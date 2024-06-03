import random
import numpy as np
from providers import ConfigProvider
from .base_generator import BaseGenerator
from models import GeoBoundingBox
from models import Location, SuspiciousLocationVariant
from utils import random_uniform_union
from typing import Dict


class LocationsGenerator(BaseGenerator):
    # Format: (min_latitude, max_latitude, min_longitude, max_longitude)
    USA_BOUNDING_BOX = GeoBoundingBox(24.396308, 49.384358, -125.0, -66.93457)
    # Range in degrees between Colorado and Kansas (Longitude)
    MAX_RADIUS = 5
    MAX_RADIUS_DEVIATION = 5
    MAX_OUTLIER_RADIUS_DEVIATION = 10

    generated_locations_by_cards: Dict[int, Location] = dict()

    def normalize_location_by_bounding_box(self, location: Location) -> Location:
        normalized_lat = max(min(
            location.latitude, self.USA_BOUNDING_BOX.max_latitude), self.USA_BOUNDING_BOX.min_latitude)
        normalized_long = max(min(
            location.longitude, self.USA_BOUNDING_BOX.max_longitude), self.USA_BOUNDING_BOX.min_longitude)

        return Location(normalized_lat, normalized_long)

    def get_suspicious_latitude_offset(self, base_latitude: float) -> float:
        while True:
            lat_offset = random_uniform_union(-self.MAX_RADIUS - self.MAX_RADIUS_DEVIATION, -
                                              self.MAX_RADIUS, self.MAX_RADIUS, self.MAX_RADIUS+self.MAX_RADIUS_DEVIATION)

            if self.USA_BOUNDING_BOX.is_in_latitude_range(base_latitude + lat_offset):
                return lat_offset

    def get_suspicious_longitude_offset(self, base_longitude: float) -> float:
        while True:
            lon_offset = random_uniform_union(-self.MAX_RADIUS - self.MAX_RADIUS_DEVIATION, -
                                              self.MAX_RADIUS, self.MAX_RADIUS, self.MAX_RADIUS+self.MAX_RADIUS_DEVIATION)

            if self.USA_BOUNDING_BOX.is_in_longitude_range(base_longitude + lon_offset):
                return lon_offset

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

    def generate_next_suspicious_location(self, card_id: int) -> Location:
        suspicious_variant = random.choice(list(SuspiciousLocationVariant))
        prev_location = self.generated_locations_by_cards.get(card_id)

        if prev_location is None:
            raise Exception(
                "Cannot generate suspicious location for the first card transaction")

        next_location = self.generate_next_location(card_id)

        if suspicious_variant == SuspiciousLocationVariant.LAT:
            next_location.latitude = prev_location.latitude + self.get_suspicious_latitude_offset(
                prev_location.latitude)
        elif suspicious_variant == SuspiciousLocationVariant.LON:
            next_location.longitude = prev_location.longitude + self.get_suspicious_longitude_offset(
                prev_location.longitude)
        elif suspicious_variant == SuspiciousLocationVariant.BOTH:
            next_location.latitude = prev_location.latitude + self.get_suspicious_latitude_offset(
                prev_location.latitude)
            next_location.longitude = prev_location.longitude + self.get_suspicious_longitude_offset(
                prev_location.longitude)

        self.generated_locations_by_cards[card_id] = next_location
        return next_location

    def generate_outlier_location(self, card_id: int) -> Location:
        suspicious_variant = random.choice(list(SuspiciousLocationVariant))

        next_location: Location = self.generate_next_location(card_id)
        outlier_lon = random_uniform_union(
            self.USA_BOUNDING_BOX.min_longitude-self.MAX_OUTLIER_RADIUS_DEVIATION, self.USA_BOUNDING_BOX.min_longitude, self.USA_BOUNDING_BOX.max_longitude+1, self.USA_BOUNDING_BOX.max_longitude+self.MAX_OUTLIER_RADIUS_DEVIATION)
        outlier_lat = random_uniform_union(
            self.USA_BOUNDING_BOX.min_latitude-self.MAX_OUTLIER_RADIUS_DEVIATION, self.USA_BOUNDING_BOX.min_latitude, self.USA_BOUNDING_BOX.max_latitude+1, self.USA_BOUNDING_BOX.max_latitude+self.MAX_OUTLIER_RADIUS_DEVIATION)

        if suspicious_variant == SuspiciousLocationVariant.LAT:
            next_location.latitude = outlier_lat
        elif suspicious_variant == SuspiciousLocationVariant.LON:
            next_location.longitude = outlier_lon
        elif suspicious_variant == SuspiciousLocationVariant.BOTH:
            next_location.latitude = outlier_lat
            next_location.longitude = outlier_lon

        self.generated_locations_by_cards[card_id] = next_location

        return next_location
