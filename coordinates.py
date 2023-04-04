from dadata import Dadata
import config

#TODO: добавить проверки на непустоту geo_lat, geo_lon, city_with_type
def get_gps_coordinates() -> dict:
    input_address = input("Введите адрес: ")
    dadata = Dadata(config.DADATA_TOKEN, config.DADATA_SECRET)
    current_address = dadata.clean(name="address", source=input_address)
    current_coordinates = {
        "current_lat": current_address["geo_lat"],
        "current_lon": current_address["geo_lon"],
        "current_city": current_address["city_with_type"]
        
    }
    return current_coordinates
