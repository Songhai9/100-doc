import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv("APP_ID")
APP_KEY = os.getenv("APP_KEY")
SHEETY_AUTH = os.getenv("SHEETY_AUTH")

HOST_DOMAIN = "https://trackapi.nutritionix.com"
SHEETY_URL = "https://api.sheety.co/04a5eb911b970feca5324c0571f9209d/copyOfMyWorkouts/workouts"


nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

sheety_headers ={
    "Authorization": SHEETY_AUTH
}

exercise_endpoint = f"{HOST_DOMAIN}/v2/natural/exercise"

exercise_query = input("What have you done today ?: ")

exercise_params = {
    "query": exercise_query
}

exercise_info = requests.post(url=exercise_endpoint, json=exercise_params, headers=nutritionix_headers)
# print(exercise_info.text)

today = datetime.now()

row_info = {
    "workout": {
        "date": today.strftime("%d/%m/%y"),
        "time": today.strftime("%H:%M:%S"),
        "exercise": exercise_info.json()["exercises"][0]["user_input"],
        "duration": exercise_info.json()["exercises"][0]["duration_min"],
        "calories": exercise_info.json()["exercises"][0]["nf_calories"]
    }
}

add_row = requests.post(url=SHEETY_URL, json=row_info, headers=sheety_headers)