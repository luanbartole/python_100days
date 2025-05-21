import requests

SHEETY_ENDPOINT = "https://api.sheety.co/b573244ba0df7b737d4e04bec7a441a6/flightDeals/prices"


class DataManager:
    """Handles all interactions with the Google Sheet via Sheety API."""

    def __init__(self, token: str):
        """
        Initializes the DataManager with an authorization token.

        Args:
            token (str): Bearer token for Sheety API access.
        """
        self.sheety_token = {
            "Authorization": f"Bearer {token}"
        }

    def get_sheet(self):
        """
        Retrieves the flight deals sheet data.

        Returns:
            list: A list of dictionaries representing each row in the sheet.
        """
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.sheety_token)
        response.raise_for_status()  # Raise error if the request failed
        sheet_data = response.json()
        return sheet_data["prices"]

    def update_sheet(self, row: dict, row_id: int):
        """
        Updates a specific row in the sheet with the IATA code.

        Args:
            row (dict): A dictionary representing a row from the sheet.
            row_id (int): The ID (row number) to update in the sheet.
        """
        new_row = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        # Send PUT request to update the sheet row with the IATA code
        response = requests.put(
            url=SHEETY_ENDPOINT + f"/{row_id}",
            headers=self.sheety_token,
            json=new_row
        )
        response.raise_for_status()  # Raise error if the request failed
