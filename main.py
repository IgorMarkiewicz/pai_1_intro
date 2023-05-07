import json
import requests

url = "https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json"

response = requests.get(url)
def httpcheck(url):
    if 400 <= response.status_code <600:
        raise Exception("blad")
    print(response)
    return response.json()

print(httpcheck(url))
