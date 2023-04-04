from dadata import Dadata
import config


INPUT_ADDRESS = "томск ленская 51 45"
dadata = Dadata(config.DADATA_TOKEN, config.DADATA_SECRET)
current_address = dadata.clean(name="address", source=INPUT_ADDRESS)

current_lat = current_address["geo_lat"]
current_lon = current_address["geo_lon"]
current_city = current_address["city_with_type"]

print(current_lat, current_lon)
