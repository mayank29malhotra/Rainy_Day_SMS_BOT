import requests
from twilio.rest import Client
api_key = "api_key for open weather map "
account_sid = "api sid for twilio "
auth_token = "api auth token for twilio "

param = {
    "lat": 28.713020,
    "lon": 77.158752,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric"

}
response = requests.get("https://api.openweathermap.org/data/2.5/onecall?", params=param)
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
        from_=" twilio virtual phone number",
        body="Mayank, It's going to rain today. Remember to bring an ☔️Have a Good Day !!",
        to='reciever phone number'
    )
    print(message.status)

else:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_=" twilio virtual phone number",
        body="Mayank, It's not going to rain today. Don't bring your Umbrella . Have a Good Day !!!",
        to='reciever phone number'
    )
    print(message.status)
