from coordinates import get_gps_coordinates
from weather_api_service import get_weather
import pprint


def main() -> dict:
    my_coordinates = get_gps_coordinates()
    my_weather = get_weather(my_coordinates)
    print()
    pprint.pprint(my_weather)


main()