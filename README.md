# About Flights
A web service that responds to GET / flight /: id and returns data from a CSV file with flight number, departure time, and arrival time in JSON format.

Example of CSV file: 
```
Id,Origin,Destination,DepartureDate,DepartureTime,ArrivalDate,ArrivalTime,Number
1,SVO,BKK,20210701,2010,20210702,1115,SU-275
```

# Quick Start
To run the web-server through the command-line:
```
python3 main.py csv_file.csv
```
To test the web-server works correctly:
```
curl http://192.168.1.9:5000/flights/2
```
# Unit Tests
To start unit tests:
```
python3 flights_test.py
```
