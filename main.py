import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "69f04e4613056b159c2761a9d9e664d2"


weather_params = {
    "lat": 50.447731,
    "lon": 30.542721,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)

print(response.status_code)
print(response.json())
