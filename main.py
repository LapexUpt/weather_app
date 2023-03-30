import requests

current_lat = 1
current_lon = 1
exclude = "current" # current/minutely/hourly/daily/alerts
open_weather_api_key = "90ecafcfe032346e5aadc13164335a8b"
url = f"https://api.openweathermap.org/data/3.0/onecall?lat={current_lat}&lon={current_lon}&exclude={exclude}&appid={open_weather_api_key}"

req = requests.get(url)
print(req)