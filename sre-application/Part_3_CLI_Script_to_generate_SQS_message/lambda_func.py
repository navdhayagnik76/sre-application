import requests
import json

URL = "http://ec2-18-237-181-119.us-west-2.compute.amazonaws.com"
API_KEY = "some_api_key"
headers = {'x-api-key': API_KEY}

with open("data.json") as f:
    data = json.load(f)

r = requests.post(URL, headers=headers, json=data)
print(r.status_code)
print(r.json())
