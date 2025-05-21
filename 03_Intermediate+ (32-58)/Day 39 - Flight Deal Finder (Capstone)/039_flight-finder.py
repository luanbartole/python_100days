import os
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch

# Load sensitive credentials from environment variables
SHEETY_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
FLIGHT_API_KEY = os.environ.get("KIWI_TEQUILA_FLIGHT_API_KEY")
ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
PHONE_A = os.environ.get("PHONE_A")
PHONE_B = os.environ.get("PHONE_B")

# Initialize service objects
notification_manager = NotificationManager(
    twilio_sid=ACCOUNT_SID,
    twilio_token=AUTH_TOKEN,
    twilio_phone_a=PHONE_A,
    twilio_phone_b=PHONE_B)
data_manager = DataManager(SHEETY_BEARER_TOKEN)
flight_search = FlightSearch(FLIGHT_API_KEY)

# Get flight data from Google Sheet
sheet_data = data_manager.get_sheet()

# Iterate over each row in the sheet
for row_id in range(len(sheet_data)):
    row = sheet_data[row_id]

    if row["iataCode"]:
        # Skip if IATA code already exists for the city
        print("IATA Codes are already filled.")
    else:
        # Write the IATA Code value for the iataCode key in the current row.
        row["iataCode"] = flight_search.get_iata_code(row["city"])
        data_manager.update_sheet(row, row_id+2)

        # Search for cheapest flight to that destination
        cheap_flight = flight_search.get_cheap_flight(row["iataCode"])

        # Send SMS alert if cheaper flight is found
        if cheap_flight.price < row["lowestPrice"]:
            notification_manager.send_sms(text = f"Low price alert! Only £{cheap_flight.price} "
                  f"to fly from {cheap_flight.origin_city}-{cheap_flight.origin_airport} "
                  f"to {cheap_flight.destination_city}-{cheap_flight.destination_airport}, "
                  f"from {cheap_flight.out_date} to {cheap_flight.return_date}.")