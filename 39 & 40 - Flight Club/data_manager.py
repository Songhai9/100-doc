import requests
from pprint import pprint
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destinationData = {}
    
    def getDestinationData(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destinationData = data["prices"]
        return self.destinationData
    
    def updateDestinationCodes(self):
        for row in self.destinationData:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }

            response = requests.put(url=f"{SHEETY_ENDPOINT}/{row['id']}",
                                    json=new_data)
            print(response.status_code, response.json())
            



