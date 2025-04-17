import requests, os
from twilio.rest import Client


# OpenWeatherMap API endpoint and credentials
OMW_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = os.getenv("OMW_API_KEY")

# Twilio credentials
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
PHONE_A = os.getenv("PHONE_A")
PHONE_B = os.getenv("PHONE_B")

# Coordinates for the forecast location
MY_LAT = -23.600670
MY_LON = -46.897388

# --- Fetch Weather Data ---
weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "cnt": 4  # Next 4 forecast blocks (each block = 3 hours)
}

response = requests.get(url=OMW_ENDPOINT, params=weather_params)
response.raise_for_status()
forecast_data = response.json()["list"]


def is_gonna_rain() -> bool:
    """
    Checks the forecast for the next 12 hours (4 blocks of 3-hour data).
    Returns True if any forecast block indicates rain (weather ID < 700).
    """
    for i, hour_data in enumerate(forecast_data):
        weather_id = hour_data["weather"][0]["id"]
        main = hour_data["weather"][0]["main"]
        desc = hour_data["weather"][0]["description"]
        print(f"{i}: {weather_id} - {main}: {desc.capitalize()}")
        if weather_id < 700:
            return True
    return False


def send_sms(text: str):
    """
    Sends an SMS using the Twilio API with the provided text message.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=text,
        from_=PHONE_A,
        to=PHONE_B
    )
    print("SMS status:", message.status)


# --- Run Forecast Check and Notify ---
if is_gonna_rain():
    send_sms("Bring an Umbrella! Rain is on the way.")
else:
    send_sms("Clear skies ahead. You're good to go!")
