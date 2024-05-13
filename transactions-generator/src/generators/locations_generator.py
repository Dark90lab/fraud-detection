import numpy as np
from providers import ConfigProvider
from .base_generator import BaseGenerator
from models import GeoBoundingBox
from models import Location
from typing import Dict


class LocationsGenerator(BaseGenerator):
    # Format: (min_latitude, max_latitude, min_longitude, max_longitude)
    USA_BOUNDING_BOX = GeoBoundingBox(24.396308, 49.384358, -125.0, -66.93457)
    # Range in degrees between Colorado and Kansas (Longitude)
    MAX_RADIUS = 15

    generated_locations_by_cards: Dict[int, Location] = dict()

    # def __init__(self, config_provider: ConfigProvider):
    #     super().__init__(config_provider)
    #     self.generated_locations_by_cards: Dict[int, Location] = dict()

    def normalize_location_by_bounding_box(self, location: Location) -> Location:
        normalized_lat = max(min(
            location.latitude, self.USA_BOUNDING_BOX.max_latitude), self.USA_BOUNDING_BOX.min_latitude)
        normalized_long = max(min(
            location.longitude, self.USA_BOUNDING_BOX.max_longitude), self.USA_BOUNDING_BOX.min_longitude)

        return Location(normalized_lat, normalized_long)

    def generate_random_location(self) -> Location:
        latitude = np.random.uniform(
            self.USA_BOUNDING_BOX.min_latitude, self.USA_BOUNDING_BOX.max_latitude)
        longitude = np.random.uniform(
            self.USA_BOUNDING_BOX.min_longitude, self.USA_BOUNDING_BOX.max_longitude)
        return Location(latitude, longitude)

    def generate_next_location(self, card_id: int) -> Location:
        prev_location = self.generated_locations_by_cards.get(card_id)

        if prev_location is None:
            next_location = self.generate_random_location()
            self.generated_locations_by_cards[card_id] = next_location
            return next_location

        lat_offset = np.random.uniform(-self.MAX_RADIUS, self.MAX_RADIUS)
        long_offset = np.random.uniform(-self.MAX_RADIUS, self.MAX_RADIUS)

        next_location = self.normalize_location_by_bounding_box(Location(
            prev_location.latitude+lat_offset, prev_location.longitude + long_offset))

        self.generated_locations_by_cards[card_id] = next_location

        return next_location
