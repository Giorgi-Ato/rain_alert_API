import requests
from twilio.rest import Client
import datetime
from data import compliments


END_POINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a86058055fc6f6c0949ebed75cbe3c8a"
lat = 41.616756
lon = 41.636745

account_sid = "AC82c6254fb51a807858cbe12be77bdf02"
auth_token = "3e51ef26d5d54336ecba54aa8127e861"


parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "lang": "ua",
    "units": "metric",
}

response = requests.get(url=END_POINT, params=parameters)
response.raise_for_status()
data = response.json()

weather = data['weather'][0]['description']
temp = data['main']['temp']

sms = f"Доброго дня Аліна. Сьогодні очікується {weather}. температура повітря буде {temp} градусів. " \
      + compliments[datetime.datetime.now().day] + " З любов'ю Гіоргі. ❤❤❤"

client = Client(account_sid, auth_token)
message = client.messages \
            .create(
                 body=sms,
                 from_='+19852832957',
                 to='+995568502548',
             )
