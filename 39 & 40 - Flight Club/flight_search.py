import os
from dotenv import load_dotenv
import requests
from pprint import pprint

load_dotenv()

AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
AMADEUS_URL = "https://test.api.amadeus.com/v1"
SEARCH_BY_CITY_ENDPOINT = "/reference-data/locations/cities"

class FlightSearch:
    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.api_secret = os.getenv("AMADEUS_SECRET")
        self.token = self._getToken()

    def getDestinationCode(self, keyword):
        amadeus_headers = {
            "Authorization": f"Bearer {self.token}"
        }
        response = requests.get(
            url=f"{AMADEUS_URL}/{SEARCH_BY_CITY_ENDPOINT}?keyword={keyword}", 
            headers=amadeus_headers)
        data = response.json()
        return data["data"][0]["iataCode"]
    
    def _getToken(self):
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }

        response = requests.post(url=AUTH_URL, data=body)
        if response.status_code == 200:
            access_token = response.json().get("access_token")
            return access_token
        

# flight_search = FlightSearch()
# print(flight_search.getDestinationCode(keyword="PARIS"))