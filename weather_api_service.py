from requests import get
import config


def get_weather(latitude, longitude, city):
    params = f"?lat={latitude}&lon={longitude}&appid={config.OPEN_WEATHER_API_KEY}"
    response = get(config.OPEN_WEATHER_URL + params)
    weather_model = {
        "city": city,
        "weather": response["weather"]["main"],
        "detailed_weather": response["weather"]["description"],
        "temp": response["main"]["temp"],
        "temp_feels": response["main"]["feels_like"],
    }
    return weather_model



print(type(get_weather(56, 84, "г Томск")))
print(get_weather(56, 84, "г Томск"))