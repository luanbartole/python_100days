import requests
from datetime import datetime
import os

# API endpoints for Nutritionix (exercise data) and Sheety (Google Sheets integration)
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/8fc3a2a3a73c54c49c4ccd24815057c5/workoutTracking/workouts"

# Environment variables for API authentication
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")

# Current date and time
today = datetime.now()

# Request headers for Nutritionix
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

# Authorization header for Sheety
sheety_token = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}"
}

# User input for exercise tracking
exercise_params = {
    "query": input("Exercises done: "),
    "gender": "male",
    "weight_kg": 85,
    "height_cm": 175,
    "age": 21
}

def add_row(exercise: dict):
    """
    Sends a POST request to Sheety to log the given exercise data into a Google Sheet.

    Parameters:
        exercise (dict): A dictionary containing exercise details from Nutritionix.
    """
    new_row = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheety_response = requests.post(url=SHEETY_ENDPOINT, json=new_row, headers=sheety_token)
    print(sheety_response.status_code)


# Request exercise data from Nutritionix based on user input
exercise_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=nutritionix_headers)
print(exercise_response.status_code)

# Send each exercise result to Google Sheets
exercise_data = exercise_response.json()
for exercise in exercise_data["exercises"]:
    add_row(exercise)
