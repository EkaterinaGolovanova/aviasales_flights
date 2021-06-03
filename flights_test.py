import unittest
import json

from flights import Flights


class TestFlights(unittest.TestCase):
    def test_base(self):
        csv_file = 'csv_file.csv'
        flight_id = 1
        expected = '{'\
                   '\n    "Number": "SU-275",'\
                   '\n    "DepartureTime": "2010",'\
                   '\n    "ArrivalTime": "1115"'\
                   '\n}'
        flights = Flights(csv_file)
        actual = flights.search_flight(flight_id)
        self.assertEqual(actual, expected)

    def test_no_id(self):
        csv_file = 'csv_file.csv'
        flight_id = 10
        expected = None
        flights = Flights(csv_file)
        actual = flights.search_flight(flight_id)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()