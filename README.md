AI in Business Project

Overview
This project is designed to assist businesses in making informed decisions by analyzing key economic indicators and providing actionable insights. The system leverages artificial intelligence to process and predict the following:

Unemployment Rate and Consumer Price Index (CPI) for the next month.
Business expansion or defensive strategies based on these economic indicators.
Client location analysis, including performance changes month-to-month.
Summarization of relevant business articles to keep owners informed.

Features

Economic Analysis:
Analyzes and visualizes unemployment rate and CPI.
Predicts trends for these indicators for the next month using AI.
Provides recommendations on business strategies based on the predictions (e.g., expansion or defensive measures).

Client Location Insights:
Displays data for two client locations.
Shows how client performance has increased or decreased compared to the previous month.

Article Summarization:
Reads and summarizes business-related articles using AI.
Helps business owners stay updated and make timely decisions.

Getting Started.

1. Clone the Repository:
git clone <repository-url>
cd <repository-directory>

2. Install Dependencies:
Make sure you have Python and Node.js installed. Then, install the necessary Python packages and Node.js modules:
pip install -r requirements.txt
npm install


3. Set Up the Environment:
Update the config.json file with your specific settings.

4. Run the Application:
Start the Python backend:
python generate_locaton.py
python prediction.py
python scrap.py
For the frontend, use the following command to build and watch for changes:
npm run build.
or launch live server for dashboard.html (install live extension on vs code)

6. Access the Application:
Open your browser and navigate to http://localhost:8000 (or the port specified in your configuration) to view the dashboard and insights.

Project Structure
* public/: Contains HTML files and the compiled CSS.
* src/: Includes input CSS with Tailwind directives, and JavaScript files.
* scripts/: Contains Python scripts for data processing and visualization.
* node_modules/: Contains Node.js modules.
* package.json: Includes scripts and dependencies for the frontend.
* postcss.config.js: Configuration for PostCSS.
* tailwind.config.js: Configuration for Tailwind CSS.
* README.md: This file.

How It Works

1. Data Analysis:
Economic data is fetched and processed to create visualizations.
Predictions are made for the next month using AI models trained on historical data.

2. Client Insights:
* Location data is analyzed to determine changes in client performance month-over-month.
* Results are displayed on the dashboard.

3. Article Summarization:
* Business articles are read and summarized using natural language processing (NLP) models.
* Summaries are provided to help business owners stay informed.

Contributing:
this project is not open for contributions(only the group members can contribute) as it is for NERDMA hackathon.

License
This project is licensed under the MIT License.

Contact
For any questions or support, please reach out to innocentaphane12@gmail.com
