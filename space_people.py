# Demo: Create a Python Virtual Environment
import requests

people = requests.get("http://api.open-notify.org/astros.json")
json = people.json()

print("The people currently in space are:")
for people in json["people"]:
    print(people["name"])
