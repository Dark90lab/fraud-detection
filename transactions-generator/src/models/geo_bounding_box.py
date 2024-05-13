class GeoBoundingBox:
    def __init__(self, min_lat: float, max_lat: float, min_long: float, max_long: float) -> None:
        self.min_latitude = min_lat
        self.max_latitude = max_lat
        self.min_longitude = min_long
        self.max_longitude = max_long
