import requests
import json


def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)

print("\nUnformatted Output:")
print(response.text)

print("\nFormatted Output:")
jprint(response.json())
