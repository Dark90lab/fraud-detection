from utils import Serializable


class Location(Serializable):
    def __init__(self, latitude, longitude) -> None:
        self.latitude = latitude
        self.longitude = longitude

    def to_dict(self):
        return {
            'lat': self.latitude,
            'long': self.longitude
        }
