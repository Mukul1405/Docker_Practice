import requests

response = requests.get("http://flaskapp:81")
print(response.text)