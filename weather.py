from coordinates import get_gps_coordinates
from weather_api_service import get_weather


def main() -> str:
    my_coordinates = get_gps_coordinates()    
    my_weather = get_weather(my_coordinates)
    print(my_weather)


flag = False
while not flag:
    main()
    print()
    answer = input("Узнать погоду где-то еще? Y/N ")
    if answer == "Y":
        flag
    else:
        break
