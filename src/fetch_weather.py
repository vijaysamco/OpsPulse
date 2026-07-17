import requests
import json
import os

url = (
    "https://api.open-meteo.com/v1/forecast"
    "?latitude=13.08"
    "&longitude=80.27"
    "&current=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

response = requests.get(url)
data = response.json()

os.makedirs("data", exist_ok=True)

with open("data/raw_weather.json", "w") as f:
    json.dump(data, f, indent=4)

print("Raw JSON saved successfully!")