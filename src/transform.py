import json
import pandas as pd

with open("data/raw_weather.json") as f:
    weather = json.load(f)

current = weather["current"]

df = pd.DataFrame({
    "Time": [current["time"]],
    "Temperature": [current["temperature_2m"]],
    "Humidity": [current["relative_humidity_2m"]],
    "WindSpeed": [current["wind_speed_10m"]]
})

df.to_csv("data/weather.csv", index=False)

print(df)