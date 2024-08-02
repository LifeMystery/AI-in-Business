import json
from collections import Counter

def get_top_two_locations(locations):
    location_counts = Counter(locations)
    return location_counts.most_common(2)

def calculate_growth(previous_total, current_total):
    if previous_total == 0:
        return 0, "up"  # Avoid division by zero, assume 100% growth if no previous data
    change = current_total - previous_total
    percentage_change = (change / previous_total) * 100
    trend = "up" if change > 0 else "down" if change < 0 else "up"
    return percentage_change, trend

def main():
    prev_total_users = 16  # Example previous total users, replace with actual value if available
    user_locations = [
        "Rosebank", "Daveyton", "Rosebank", "Cape Town", "Cape Town",
        "Pretoria", "Mpumalanga", "Rosebank", "Pretoria", "Pretoria"
    ]
    current_total_users = len(user_locations)
    percentage_change, trend = calculate_growth(prev_total_users, current_total_users)

    top_two_locations = get_top_two_locations(user_locations)
    top_two_json = [{'name': location, 'count': count} for location, count in top_two_locations]
    
    data_to_save = {
        "top_locations": top_two_json,
        "trend": trend,
        "percentage": percentage_change,
        "current_total_users": current_total_users
    }

    with open('locations.json', 'w') as f:
        json.dump(data_to_save, f, indent=4)
    
    print("Top 2 common locations:")
    for location, count in top_two_locations:
        print(f"{location}: {count} occurrences")

if __name__ == "__main__":
    main()
