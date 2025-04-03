# Demo: Use the Open Weather Map API
import requests

city = "London"
url = (
    "http://api.weatherapi.com/v1/current.json?key=32654e4fc63c43658e9205614250304&q="
    + city
    + "&aqi=no"
)
response = requests.get(url)
weather_json = response.json()

city = weather_json["location"]["name"]
temp = weather_json["current"]["temp_f"]
description = weather_json["current"]["condition"]["text"]
print(
    "The current weather in",
    city,
    "is",
    str(temp) + "°F",
    "and",
    description.lower() + "!",
)
