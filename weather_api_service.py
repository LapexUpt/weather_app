from requests import get

def get_weather(latitude, longitude, opw_api_key):
    opw_api_key = "90ecafcfe032346e5aadc13164335a8b"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = f"?lat={latitude}&lon={longitude}&appid={opw_api_key}"
    weather = get(url + params)
    return weather