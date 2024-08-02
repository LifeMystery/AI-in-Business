import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures, MinMaxScaler
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import os
import json

# File paths
unemployment_rate_path = 'unemployment_rate.png'
cpi_path = 'cpi.png'
output_path = 'output.json'

# Delete existing files if they exist
if os.path.exists(unemployment_rate_path):
    os.remove(unemployment_rate_path)
if os.path.exists(cpi_path):
    os.remove(cpi_path)
if os.path.exists(output_path):
    os.remove(output_path)

# Sample data
data = {
    'unemployment_rate': [10, 19, 15, 12, 11, 16, 14, 13, 17, 20, 18, 16, 12, 14, 13, 15, 18, 17, 16, 14, 13, 12, 14, 16],
    'cpi': [2.3, 2.5, 2.7, 2.8, 3.0, 2.9, 2.6, 2.7, 2.8, 2.9, 3.1, 3.2, 3.0, 2.8, 2.7, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7]
}

# Convert the data into a pandas DataFrame
df = pd.DataFrame(data)
df.index = pd.date_range(start='2022-01-01', periods=len(df), freq='ME')

# Predict next month's value for both unemployment_rate and cpi
def predict_next_month(data):
    X = np.arange(len(data)).reshape(-1, 1)
    y = np.array(data)

    # Polynomial regression for better trend fitting
    poly = PolynomialFeatures(degree=2)
    X_poly = poly.fit_transform(X)
    model = LinearRegression()
    model.fit(X_poly, y)
    next_index = np.arange(len(data) + 1).reshape(-1, 1)
    next_index_poly = poly.transform(next_index)
    prediction = model.predict(next_index_poly)
    return next_index, prediction

# Get predictions
next_unemployment_index, next_unemployment_prediction = predict_next_month(df['unemployment_rate'])
next_cpi_index, next_cpi_prediction = predict_next_month(df['cpi'])

# Convert index to a numpy array
df_dates = df.index.to_numpy()

# Save plots
plt.figure(figsize=(14, 6))

# Unemployment Rate Plot
plt.subplot(1, 2, 1)
plt.plot(df_dates, df['unemployment_rate'].values, marker='o', label='Actual Unemployment Rate', linestyle='-')
plt.plot(pd.date_range(start='2022-01-01', periods=len(next_unemployment_prediction), freq='ME').to_numpy(), next_unemployment_prediction, linestyle='--', color='red', label='Predicted Unemployment Rate')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.title('Unemployment Rate Over Time')
plt.grid(True)
plt.legend()
plt.savefig(unemployment_rate_path)  # Save the unemployment rate plot

# CPI Plot
plt.subplot(1, 2, 2)
plt.plot(df_dates, df['cpi'].values, marker='o', color='orange', label='Actual CPI', linestyle='-')
plt.plot(pd.date_range(start='2022-01-01', periods=len(next_cpi_prediction), freq='ME').to_numpy(), next_cpi_prediction, linestyle='--', color='green', label='Predicted CPI')
plt.xlabel('Date')
plt.ylabel('CPI')
plt.title('CPI Over Time')
plt.grid(True)
plt.legend()
plt.savefig(cpi_path)  # Save the CPI plot

plt.tight_layout()
plt.show()

# Predict next values
next_unemployment_rate = next_unemployment_prediction[-1]
next_cpi = next_cpi_prediction[-1]

print(f"Predicted Unemployment Rate for Next Month: {next_unemployment_rate:.2f}%")
print(f"Predicted CPI for Next Month: {next_cpi:.2f}")

# Determine trend percentage
def determine_trend_percentage(unemployment_rate, cpi):
    avg_unemployment_rate = np.mean(df['unemployment_rate'])
    avg_cpi = np.mean(df['cpi'])

    # Calculate trend scores
    unemployment_score = (avg_unemployment_rate - unemployment_rate) / (avg_unemployment_rate - min(df['unemployment_rate']))
    cpi_score = (cpi - min(df['cpi'])) / (max(df['cpi']) - min(df['cpi']))

    # Combine scores into a percentage
    trend_percentage = (unemployment_score + cpi_score) / 2 * 100
    return trend_percentage

overall_trend_percentage = determine_trend_percentage(next_unemployment_rate, next_cpi)
print(f"Overall Trend Percentage: {overall_trend_percentage:.2f}%")

# Determine if trend is positive or negative
if overall_trend_percentage > 50:
    trend_description = "Positive"
else:
    trend_description = "Negative"

print(f"Overall Trend: {trend_description}")

# Normalize the data for neural network
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df)

# Prepare the dataset for neural network
X = np.arange(len(df)).reshape(-1, 1)
y = scaled_data

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Create the neural network model
model = Sequential([
    Dense(64, input_dim=1, activation='relu'),
    Dense(32, activation='relu'),
    Dense(2)  # Output layer for both unemployment rate and CPI
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model
model.fit(X_train, y_train, epochs=100, batch_size=1, verbose=1)

# Predict the next month's values using the neural network
next_index = np.array([[len(df)]])
scaled_predictions = model.predict(next_index)

# Inverse transform to get actual values
predictions = scaler.inverse_transform(scaled_predictions)

# Extract predictions
predicted_unemployment_rate_nn = predictions[0, 0]
predicted_cpi_nn = predictions[0, 1]

print(f"Neural Network Predicted Unemployment Rate for Next Month: {predicted_unemployment_rate_nn:.2f}%")
print(f"Neural Network Predicted CPI for Next Month: {predicted_cpi_nn:.2f}")

# Example threshold values for business decisions
cpi_threshold_high = 3.5
cpi_threshold_low = 3.0
unemployment_threshold_high = 15.0
unemployment_threshold_low = 12.0

def generate_business_tips(predicted_unemployment_rate, predicted_cpi, trend_percentage):
    tips = []
    
    if predicted_cpi > cpi_threshold_high:
        tips.append("Consider increasing prices due to high CPI.")
    elif predicted_cpi < cpi_threshold_low:
        tips.append("Consider decreasing prices to attract more customers.")

    if predicted_unemployment_rate > unemployment_threshold_high:
        tips.append("Be cautious with expansion plans due to high unemployment.")
    elif predicted_unemployment_rate < unemployment_threshold_low:
        tips.append("It might be a good time to expand your business.")

    if trend_percentage > 50:
        tips.append("The overall trend is positive; consider aggressive expansion strategies.")
    else:
        tips.append("The overall trend is negative; it might be wise to consolidate and optimize.")

    return tips

# Generate business tips based on neural network predictions
business_tips = generate_business_tips(predicted_unemployment_rate_nn, predicted_cpi_nn, overall_trend_percentage)
for tip in business_tips:
    print(tip)

# Save output to JSON file
output_data = {
    "predicted_unemployment_rate_nn": f"{predicted_unemployment_rate_nn:.2f}%",
    "predicted_cpi_nn": f"{predicted_cpi_nn:.2f}",
    "overall_trend_percentage": f"{overall_trend_percentage:.2f}%",
    "overall_trend": trend_description,
    "business_tips": business_tips
}

with open(output_path, 'w') as json_file:
    json.dump(output_data, json_file, indent=4)
