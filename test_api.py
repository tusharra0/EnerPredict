import requests

url = "http://127.0.0.1:5000/predict"

data = {
    "X1": 0.9,
    "X2": 563.5,
    "X3": 318.5,
    "X4": 122.5,
    "X5": 7,
    "X6": 2,
    "X7": 0.0,
    "X8": 0
}

response = requests.post(url, json=data)

if response.status_code == 200:
    print("Successful")
    print(response.json())
else:
    print("Unsucessful")
    print(response.json())
