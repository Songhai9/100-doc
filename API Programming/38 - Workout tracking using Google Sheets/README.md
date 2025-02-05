# Workout Tracker

This project tracks your workouts by accepting a text description of your exercises, fetching relevant workout data from the Nutritionix API, and then logging the details (date, time, exercise, duration, and calories) to a Google Sheet via Sheety.

## Features

- Parse a user's workout input.
- Retrieve exercise details from the Nutritionix API.
- Automate logging to a Google Sheet using the Sheety API.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```

## Setup

1. **Environment Variables**: Create a `.env` file in the project root with your credentials:
    ```
    NUTRITIONIX_ID='your_nutritionix_app_id'
    NUTRITIONIX_KEY='your_nutritionix_api_key'
    SHEETY_BEARER='Bearer your_sheety_bearer_token'
    ```

## Usage

Run the project by executing `main.py`:
```
python main.py
```
Follow the prompt to input a description of your workout. The program will then log the details to your Google Sheet.

