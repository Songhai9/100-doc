import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

user_token = os.getenv('USER_TOKEN')
username = 'oumar'
pixela_endpoint = 'https://pixe.la/v1/users'

headers = {
    "X-USER-TOKEN": user_token
}

user_params = {
    'token':user_token,
    'username':username,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}

user_response = requests.post(url=pixela_endpoint, json=user_params)
print(user_response.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'
graph_params = {
    "id":"graph1",
    "name":"coding graph",
    "unit":"hours",
    "type":"float",
    "color":"ichou"
}

graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(graph_response.text)
today = datetime.today().strftime("%Y%m%d")

update_endpoint = f'{graph_endpoint}/{graph_params['id']}'
quantity = input('How many hours did you code today ?')
update_params = {
    "date":today,
    "quantity":quantity,
}

pixel_response = requests.post(url=update_endpoint, json=update_params, headers=headers)
print(pixel_response.text)