import os
import requests
import datetime as dt
from twilio.rest import Client

# API Endpoints and Credentials
MARKETSTACK_API_ENDPOINT = "http://api.marketstack.com/v1/eod"
MARKETSTACK_API_KEY = os.getenv("MARKETSTACK_API_KEY")
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
PHONE_A = os.getenv("PHONE_A")
PHONE_B = os.getenv("PHONE_B")

# Stock Monitoring Configuration
THRESHOLD = 2  # percentage change threshold for triggering alerts
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def stock_price_diff():
    """
    Calculates the percentage difference between the closing prices of a stock
    from two consecutive previous days.

    Returns:
        int: Rounded percentage difference in closing prices.
    """
    yesterday = str((dt.datetime.now() - dt.timedelta(1)))[:10]
    two_days_ago = str((dt.datetime.now() - dt.timedelta(2)))[:10]

    params = {
        "access_key": MARKETSTACK_API_KEY,
        "symbols": STOCK,
        "date_from": two_days_ago,
        "date_to": yesterday
    }

    response = requests.get(MARKETSTACK_API_ENDPOINT, params)
    response.raise_for_status()
    data = response.json()["data"]

    yesterday_close = data[0]["close"]
    two_days_ago_close = data[1]["close"]

    percent_diff = round(((yesterday_close - two_days_ago_close) / two_days_ago_close) * 100)
    return percent_diff


def send_sms(text: str):
    """
    Sends an SMS containing the provided message body via Twilio.

    Args:
        text (str): The body of the SMS to be sent.
    """
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=text,
        from_=PHONE_A,
        to=PHONE_B
    )
    print(message.status)


# Check price movement and send SMS if threshold is crossed
price_change = stock_price_diff()

if abs(price_change) > THRESHOLD:
    direction = "🔺" if price_change > 0 else "🔻"
    sms_body = f"{STOCK}: {direction}{abs(price_change)}%"
    send_sms(sms_body)
