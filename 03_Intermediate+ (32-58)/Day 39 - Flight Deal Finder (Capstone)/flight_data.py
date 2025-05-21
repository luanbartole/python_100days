class FlightData:
    """Stores structured information about a flight deal."""

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        """
        Initializes a FlightData object with details of a flight.

        Args:
            price (float): Price of the flight in GBP.
            origin_city (str): Name of the departure city.
            origin_airport (str): IATA code of the departure airport.
            destination_city (str): Name of the arrival city.
            destination_airport (str): IATA code of the arrival airport.
            out_date (str): Departure date (format: YYYY-MM-DD).
            return_date (str): Return date (format: YYYY-MM-DD).
        """
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
