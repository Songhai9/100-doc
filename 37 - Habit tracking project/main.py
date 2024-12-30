import requests
from datetime import datetime

TOKEN = "sometokenhere"
USERNAME = "songhai"

pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
    "id": "graph1",
    "name": "coding graph",
    "unit": "hours",
    "type": "float",
    "color": "ajisai"
}

pixel_endpoint = f"{graph_endpoint}/{graphs_config['id']}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "4",
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)
