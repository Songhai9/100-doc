# IMPORTS
import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

# GET ENVIRONMENT VARIABLES
load_dotenv()
my_lon = 48.573406
my_lat = 7.752111
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")


# API ENDPOINTS AND FETCHING DATA
open_weather_api_key = os.getenv("OPEN_WEATHER_API_KEY")
open_weather_endpoint = " https://api.openweathermap.org/data/2.5/forecast"
params = {"lon": my_lon, "lat": my_lat, "appid": open_weather_api_key, "cnt": 4}
response = requests.get(url=open_weather_endpoint, params=params)
response.raise_for_status()
weather_data = response.json()

# CHECKING IF IT RAINS AND SENDING A MESSAGE IF SO
for forecast in weather_data["list"]:
    if forecast["weather"][0]["id"] < 700:
        client = Client(account_sid, auth_token)
        print("Will rain, bring an umbrella")
        message = client.messages.create(
            from_="+15077365218",
            body="Bring an umbrella ☂, it' going to rain",
            to="+33768412754",
        )
        print(message.sid)
        print(message.status)
        break
