# Import necessary libraries
import requests  # Used to make HTTP requests to APIs
import smtplib   # Used to send emails using SMTP
import time      # Used to create delays in the while loop
from datetime import datetime  # Used to get current local time

# User credentials for sending the email
user_email = "email@gmail.com"
user_password = "password"
target_email = "email@gmail.com"

# Coordinates roughly in the center of Brazil
MY_LAT = -14.235004
MY_LNG = -51.925282


def iss_is_overhead():
    """
    Checks if the International Space Station (ISS) is currently overhead
    within a ±5 degree range from the user's location.
    """
    # Request ISS current position from Open Notify API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    # Extract ISS position
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])

    # Check if ISS is within ±5 degrees of user's location
    if MY_LNG - 5 <= longitude <= MY_LNG + 5 and MY_LAT - 5 <= latitude <= MY_LAT + 5:
        return True
    else:
        return False


def is_night():
    """
    Determines whether it is currently nighttime at the user's location.
    Uses the Sunrise-Sunset API.
    """
    # Parameters for API: location and unformatted UTC time
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }

    # Request sunrise and sunset data
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    # Extract the hour (in UTC) and adjust for Brazil timezone (UTC-3)
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) - 3
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0]) - 3

    # Get the current hour (in local time)
    time_now = datetime.now().hour

    # Return True if it's currently nighttime
    if time_now >= sunset_hour or time_now <= sunrise_hour:
        return True
    else:
        return False


# Continuously check every 60 seconds if ISS is overhead and it's nighttime
while True:
    if iss_is_overhead() and is_night():
        # If both conditions are met, send an email alert
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user_email, user_password)  # Login to the email server
            connection.sendmail(
                from_addr=user_email,
                to_addrs=target_email,
                msg=(
                    "Subject: ISS Right Above You! Go Look Outside! \n\n"
                    "The ISS is close to your location in this great night!\n"
                    "Try to spot it in the sky outside."
                )
            )
    # Wait 60 seconds before checking again
    time.sleep(60)
