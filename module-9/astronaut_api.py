import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = "http://api.open-notify.org/astros.json"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nUnformatted Output:")
print(data)

print("\nFormatted Output:")
jprint(data)
