class GeoBoundingBox:
    def __init__(self, min_lat: float, max_lat: float, min_long: float, max_long: float) -> None:
        self.min_latitude = min_lat
        self.max_latitude = max_lat
        self.min_longitude = min_long
        self.max_longitude = max_long

    def is_in_latitude_range(self, latitude: float) -> bool:
        return latitude >= self.min_latitude and latitude <= self.max_latitude

    def is_in_longitude_range(self, longitude: float) -> bool:
        return longitude >= self.min_longitude and longitude <= self.max_longitude
