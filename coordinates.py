from dataclasses import dataclass

@dataclass(slots=True, frozen=True)
class Coordinates:
    latitude: float
    longitude: float


def get_gps_coordinates():   
    return Coordinates(latitude=44.34, longitude=10.99)
