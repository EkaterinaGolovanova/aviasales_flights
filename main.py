#!/usr/bin/env python3

import os
import sys

from flask import Flask, abort, jsonify

from flights import Flights

# Get csv file
try:
    csv_file = sys.argv[1]
    if os.path.exists(csv_file):
        flights = Flights(csv_file)
    else:
        print(f"File '{csv_file}' doesn't exist.")
        sys.exit(1)
except IndexError:
    print("Error: Please, provide a csv file name.")
    sys.exit(1)

app = Flask(__name__)


# Start web server
@app.route('/flights/<int:flight_id>', methods=['GET'])
def process_request_get_flight(flight_id: int):
    flight = flights.search_flight(flight_id)
    if flight is None:
        abort(404, description="Flight id not found")
    return flight


@app.errorhandler(404)
def flight_id_not_found(error):
    return jsonify(error=str(error)), 404


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
