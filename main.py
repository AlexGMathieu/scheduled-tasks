import requests
from twilio.rest import Client


MY_LAT = 47.497913
MY_LONG = 19.040236
api_key = os.environ.get("OWM_API_KE")

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "cnt": 4,
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
# codes = []
# for i in range(0,4):
#     codes.append(weather_data["list"][i]["weather"][0]["id"])
# codes = [weather_data["list"][i]["weather"][0]["id"] for i in range (0,4)]
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Il va pleuvoir, prends ton parapluie",
        from_="whatsapp:+14155238886",
        to="whatsapp:+33675295991",
    )

    print(message.status)
