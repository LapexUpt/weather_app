from dadata import Dadata
import config


def get_gps_coordinates() -> dict:
    coordinates_exist = False
    while not coordinates_exist:
        input_address = input("Введите адрес: ")
        dadata = Dadata(config.DADATA_TOKEN, config.DADATA_SECRET)
        current_address = dadata.clean(name="address", source=input_address)
        if not current_address["geo_lat"] or not current_address["geo_lon"]:
            print("Координаты введенного адреса не найдены. Попробуйте еще раз\n")
        else:
            coordinates_exist
            current_coordinates = {
                    "current_lat": current_address["geo_lat"],
                    "current_lon": current_address["geo_lon"]
                    
            }
            if not current_address["city_with_type"]:
                current_coordinates["current_city"] = current_address["region_with_type"]
            else:    
                current_coordinates["current_city"] = current_address["city_with_type"]
        break
    
    return current_coordinates
