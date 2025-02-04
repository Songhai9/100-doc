# Weather SMS Notifier

This project checks the weather forecast using the OpenWeatherMap API and sends an SMS via Twilio if rain is expected. 

## Features

- Retrieves a 4-point forecast for a specified location.
- Parses weather data to check for rain.
- Sends an SMS alert when rain is forecasted.

## Prerequisites

- Python 3.6+
- A verified Twilio account with a valid phone number.
- An OpenWeatherMap API key.

## Installation

1. Install the required packages:
    ```
    pip install -r requirements.txt
    ```

2. Create a `.env` file in the project root with the following content:
    ```
    OPEN_WEATHER_API_KEY='your_open_weather_api_key'
    TWILIO_SID='your_twilio_sid'
    TWILIO_AUTH_TOKEN='your_twilio_auth_token'
    ```

## Usage

Run the script (set the longitude and the latitude at the right place, you can easily
find yours at https://www.latlong.net):
```
python main.py
```
The script will perform the following steps:
- Load environment variables.
- Fetch weather data using OpenWeatherMap.
- Evaluate the weather conditions.
- Send an SMS alert via Twilio if rain is forecasted.


