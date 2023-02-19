import requests

url = "https://api.example.com/endpoint"
API_KEY = "fcdb0dc9da2f41e8ad3c2c506fccf12f"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Do something with the data returned from the API
else:
    print("Request failed with status code:", response.status_code)
