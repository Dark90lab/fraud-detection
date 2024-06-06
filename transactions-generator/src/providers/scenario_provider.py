from os import getenv
from typing import Dict
from models import FraudType


class TimeRange:
    DELIMITER = ","

    def __init__(self, range: str):
        parsed_range = range.split(self.DELIMITER)
        if len(parsed_range) != 2:
            raise Exception(
                f"Invalid Time Range: {range}, there should be two floats splitted by {self.DELIMITER}")
        self._from = float(parsed_range[0])
        self._to = float(parsed_range[1])


class FraudProbabilitiesAdapter:
    def get_probabilities() -> Dict[FraudType, float]:
        result = {
            FraudType.VALUE_TRESHOLD: float(
                getenv("VALUE_TRESHOLD_FRAUDS_PROB")),
            FraudType.LOCATION_OUTLIER: float(
                getenv("LOCATION_OUTLIER_FRAUDS_PROB")),
            FraudType.LOCATION_TRESHOLD: float(
                getenv("LOCATION_TRESHOLD_FRAUDS_PROB"))
        }

        cumulative_probabilities = sum(result.values())

        if cumulative_probabilities > 1:
            raise Exception(
                f"All fraud probabilities must be summed to at most 1!, obtained: {cumulative_probabilities}")

        result[FraudType.NONE] = 1 - cumulative_probabilities

        return result


class ScenarioProvider:
    ORDINARY_TRAN_TIME_RANGE: TimeRange
    VALUE_TRESHOLD_FRAUDS_TIME_RANGE: TimeRange

    frauds_probabilities: Dict[FraudType,
                               float]

    def __init__(self):

        self.MIN_VALUE_AMOUNT = float(getenv("MIN_VALUE_AMOUNT"))

        self.ORDINARY_TRAN_TIME_RANGE = TimeRange(
            getenv("ORDINARY_TRAN_TIME_RANGE"))
        self.VALUE_TRESHOLD_FRAUDS_TIME_RANGE = TimeRange(
            getenv("VALUE_TRESHOLD_FRAUDS_TIME_RANGE"))
        self.frauds_probabilities = FraudProbabilitiesAdapter.get_probabilities()
        self.LOCATION_TRESHOLD_FRAUDS_TIME_RANGE = TimeRange(
            getenv("LOCATION_TRESHOLD_FRAUDS_TIME_RANGE"))
        self.LIMIT_PERCENT_TRESHOLD = float(getenv("LIMIT_PERCENT_TRESHOLD"))
