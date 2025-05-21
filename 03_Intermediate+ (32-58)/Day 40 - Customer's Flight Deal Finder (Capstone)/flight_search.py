import requests
from datetime import datetime, timedelta
from flight_data import FlightData

# API endpoints for location lookup and flight search
FLIGHT_LOCATION_API_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_API_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

# Define search window: today to six months from now
today = datetime.now()
six_months_from_now = today + timedelta(180)


class FlightSearch:
    """Handles communication with the Kiwi Tequila API for flight data."""

    def __init__(self, key):
        """
        Initializes the FlightSearch object with an API key.

        Args:
            key (str): Tequila API key.
        """
        self.apiKey = key
        self.headers = {"apikey": self.apiKey}

    def get_iata_code(self, city: str):
        """
        Retrieves the IATA code for a given city name.

        Args:
            city (str): City name to look up.

        Returns:
            str: The corresponding IATA airport code.
        """
        response = requests.get(
            url=FLIGHT_LOCATION_API_ENDPOINT,
            headers=self.headers,
            params={"term": city}
        )
        response.raise_for_status()
        flight_data = response.json()
        iata_code = flight_data["locations"][0]["code"]
        return iata_code

    def get_cheap_flight(self, destination_city: str):
        """
        Searches for the cheapest round-trip flight from London to a destination city.

        Args:
            destination_city (str): IATA code of the destination city.

        Returns:
            FlightData | None: FlightData object with flight info or None if no flight found.
        """
        query = {
            "fly_from": "LON",
            "fly_to": destination_city,
            "date_from": today.strftime("%d/%m/%Y"),
            "date_to": six_months_from_now.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(
            url=FLIGHT_SEARCH_API_ENDPOINT,
            headers=self.headers,
            params=query
        )
        response.raise_for_status()

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city}.")
            return None

        # Build and return a FlightData object with the relevant flight details
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        return flight_data
