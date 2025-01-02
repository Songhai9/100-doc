#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.getDestinationData()
pprint(sheet_data)

flight_search = FlightSearch()

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.getDestinationCode(keyword=row["city"].upper())

print("\n\n")

data_manager.destinationData = sheet_data
data_manager.updateDestinationCodes()
print(data_manager.destinationData)

