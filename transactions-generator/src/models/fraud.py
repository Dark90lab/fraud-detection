from enum import Enum


class FraudType(Enum):
    VALUE_TRESHOLD = 1
    LOCATION_TRESHOLD = 2
    LOCATION_OUTLIER = 3
    TRANSACTIONS_FREQUENCY = 4
    NONE = 5
