import requests
from twilio.rest import Client
from config import *

weather_params = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}


def send_text():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="Could rain today - Bring an umbrella ☔️",
            from_=FROM_NUM,
            to=TO_NUM
        )
    print(message.status)


response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
hourly_weather_list = weather_data["hourly"][0:12]

for hour_data in hourly_weather_list:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        send_text()
        break

# works but wordy
# hourly_weather_list = hourly_weather_list[0:12]
# for hour in hourly_weather_list:
#     weather_code_list = hour["weather"]
#     for code in weather_code_list:
#         #print(code["id"])
#         if code["id"] < 700:
#             print("Bring an umbrella!")
#             break
