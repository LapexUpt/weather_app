import requests
import coordinates as coord

opw_api_key = "90ecafcfe032346e5aadc13164335a8b"
url = "https://api.openweathermap.org/data/2.5/weather"
params = f"?lat={coord.curr_lat}&lon={coord.curr_lon}&appid={opw_api_key}"
req = requests.get(url + params)
print(req.text)