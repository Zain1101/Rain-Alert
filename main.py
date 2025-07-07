import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OWM_API_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
LAT = os.getenv("LAT")
LNG = os.getenv("LNG")
FROM = os.getenv("TWILIO_FROM")
TO = os.getenv("TWILIO_TO")

OM = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    'lat': LAT,
    'lon': LNG,
    'appid': api_key,
    'cnt': 4,
}

response = requests.get(url=OM, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour_data in data['list']:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain. Remember to carry the umbrella",
        from_=FROM,
        to=TO
    )
    print(message.status)
