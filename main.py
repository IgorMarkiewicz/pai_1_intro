import json
import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

response = requests.get(url)
data = response.json()
print(data)
