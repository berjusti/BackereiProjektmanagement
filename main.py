# Main ETL orchestration script

import requests  # API requests
import etl, database, models  # Custom modules


# Pseudocode - schedule ETL jobs

def main():
    # Fetch weather data from API
    weather_data = get_weather_api_data()

    # Pass data to ETL process
    etl.process_data(weather_data)


def get_weather_api_data():
    # API request to get weather data
    response = requests.get('https://weatherapi.com/data.json')

    # Extract relevant fields
    data = response.json()['temperatures']

    return data


if __name__ == '__main__':
    main()