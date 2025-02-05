# IMPORTS
import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# ENVIRONMENT VARIABLES
load_dotenv()
nutrtionix_id = os.getenv("NUTRITIONIX_ID")
nutritionix_key = os.getenv("NUTRITIONIX_KEY")
sheety_bearer = os.getenv("SHEETY_BEARER")

# PROMPT USER
user_input = input("What have you done today ?")

# FETCHING DATA
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_headers = {"x-app-id": nutrtionix_id, "x-app-key": nutritionix_key}
sheety_endpoint = (
    "https://api.sheety.co/cdd34efccfd608d8cfb9e1956e188626/copieDeMyWorkouts/workouts"
)
authorization_header = {"Authorization": sheety_bearer}
nutritionix_config = {"query": user_input}
nutritionix_response = requests.post(
    url=nutritionix_endpoint, headers=nutritionix_headers, json=nutritionix_config
)
nurtitionix_data = nutritionix_response.json()


# UPLOADING TO SHEETY
sheety_data = {
    "workout": {
        "date": datetime.now().strftime("%d/%m/%y"),
        "time": datetime.now().strftime("%H:%M:%S"),
        "exercise": nurtitionix_data["exercises"][0]["name"],
        "duration": nurtitionix_data["exercises"][0]["duration_min"],
        "calories": nurtitionix_data["exercises"][0]["nf_calories"],
    }
}
sheety_response = requests.post(
    url=sheety_endpoint, json=sheety_data, headers=authorization_header
)
