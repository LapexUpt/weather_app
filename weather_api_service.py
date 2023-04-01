from requests import get
from coordinates import Coordinates


def get_weather(coordinates: Coordinates):
    opw_api_key = "90ecafcfe032346e5aadc13164335a8b"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = f"?lat={coordinates.latitude}&lon={coordinates.longitude}&appid={opw_api_key}"
    weather = get(url + params)
    return weather