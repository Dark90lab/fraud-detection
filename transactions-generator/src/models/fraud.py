from enum import Enum


class FraudType(Enum):
    VALUE_TRESHOLD = 1
    LOCATION_TRESHOLD = 2
    TRANSACTIONS_FREQUENCY = 3
    NONE = 4
