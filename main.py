import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = "69f04e4613056b159c2761a9d9e664d2"
account_sid = "AC523828fb39100807f314531c027aee10"
auth_token = "8dfb458694cd3f627ab0608a7c66bea0"


weather_params = {
    "lat": 45.438618,
    "lon": 10.993313,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going ti rain today. Remember to bring an ☂️",
        from_='+19786788438',
        to='+380636088047'
    )

    print(message.status)

