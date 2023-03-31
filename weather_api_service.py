import requests
import coordinates as coord

excl = "current" # current/minutely/hourly/daily/alerts
opw_api_key = "90ecafcfe032346e5aadc13164335a8b"
url = "https://api.openweathermap.org/data/3.0/onecall"
params = f"?lat={coord.curr_lat}&lon={coord.curr_lat}&exclude={excl}&appid={opw_api_key}"
req = requests.get(url + params)
print(req)