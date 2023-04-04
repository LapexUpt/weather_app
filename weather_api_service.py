from requests import get
from json import loads
import config



def get_weather(coordinates) -> dict:
    latitude = coordinates["current_lat"]
    longitude = coordinates["current_lon"]
    city = coordinates["current_city"]

    params = f"?lat={latitude}&lon={longitude}&appid={config.OPEN_WEATHER_API_KEY}&units=metric"
    current_weather = loads(get(config.OPEN_WEATHER_URL + params).text)
    weather_model = {
        "city": city,
        "weather": current_weather["weather"][0]["main"],
        "detailed_weather": current_weather["weather"][0]["description"],
        "temp": round(current_weather["main"]["temp"]),
        "temp_feels": round(current_weather["main"]["feels_like"]),
    }
    return weather_model
