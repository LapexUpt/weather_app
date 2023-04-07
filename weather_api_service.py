from requests import get
from json import loads
import config



def get_weather(coordinates) -> str:
    latitude = coordinates["current_lat"]
    longitude = coordinates["current_lon"]
    params = f"?lat={latitude}&lon={longitude}&appid={config.OPEN_WEATHER_API_KEY}&units=metric"
    current_weather = loads(get(config.OPEN_WEATHER_URL + params).text)

    city = coordinates["current_city"]
    temp = round(current_weather["main"]["temp"])
    temp_feels = round(current_weather["main"]["feels_like"])
    weather_description = config.weather_data[current_weather["weather"][0]["main"]]
    
    return f"Температура в {city} {temp}. Ощущается как {temp_feels}. {weather_description}."