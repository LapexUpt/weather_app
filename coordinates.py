from dadata import Dadata


ADDRESS_STR = "томск ленская 51 45"
token = "27fd8c4db134d75020aa8f939c019bb36b756ba3"
secret = "c51b6a0036a8175a75f53b1171657230804559ea"
dadata = Dadata(token, secret)
address_pretty = dadata.clean("address", ADDRESS_STR)

curr_lat = address_pretty["geo_lat"]
curr_lon = address_pretty["geo_lon"]

print(curr_lat, curr_lon)
