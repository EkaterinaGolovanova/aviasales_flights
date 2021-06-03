import csv
import json
from typing import Optional


def _read_csv(csv_file) -> dict:
    # Read csv file and copy its data into "db"
    db = {}
    with open(csv_file) as csv_f:
        csv_reader = csv.DictReader(csv_f)
        for row in csv_reader:
            key = int(row['Id'])
            db[key] = row
    return db


class Flights:
    def __init__(self, csv_file):
        self._db = _read_csv(csv_file)

    def search_flight(self, flight_id: int) -> Optional[str]:
        flight = {}

        # Search for specified flight by flight_id
        if flight_id in self._db:
            for key in ['Number', 'DepartureTime', 'ArrivalTime']:
                flight[key] = self._db[flight_id].get(key)
        else:
            return None

        # Convert "flight" into JSON string
        json_string = json.dumps(flight, indent=4)
        return json_string