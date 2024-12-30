# Workout Tracking using Google Sheets

This project allows you to track your workouts using the Nutritionix API and store the data in a Google Sheet using the Sheety API.

## Setup

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your API keys:
    ```env
    APP_ID=<your_nutritionix_app_id>
    APP_KEY=<your_nutritionix_app_key>
    SHEETY_AUTH=<your_sheety_auth_token>
    ```

## Usage

1. Run the script:
    ```sh
    python main.py
    ```

2. When prompted, enter the exercise you did today.

3. The script will log the exercise data to your Google Sheet.

## APIs Used

- **Nutritionix API**: To get exercise data.
- **Sheety API**: To log the exercise data into a Google Sheet.
