import requests as requests


# Variables
BASE = "http://127.0.0.1:5000/"

print("----------------------------------------------------------------------------")
response = requests.post(BASE + "employee/1", {"name": "Julia Hendricks", "age": 30, "position": "CEO"})
print(response.json())
