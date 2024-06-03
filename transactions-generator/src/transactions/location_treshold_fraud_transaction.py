import numpy as np
from .transaction_base import TransactionBase
from typing import Tuple
from models import TransactionResult


class LocationTresholdFraudTransaction(TransactionBase):
    TYPE = 'LT'

    def get_result(self, value: float) -> TransactionResult:
        tran_base = super().get_result_base(value)

        return TransactionResult.fromBase(tran_base)

    def get_suspicious_waiting_time(self) -> float:
        return np.random.uniform(self.scenario.LOCATION_TRESHOLD_FRAUDS_TIME_RANGE._from, self.scenario.LOCATION_TRESHOLD_FRAUDS_TIME_RANGE._to)

    def generate(self) -> list[Tuple[float, TransactionResult]]:
        result: list[Tuple[float, TransactionResult]] = list()

        validTransaction = self.get_result(self.get_value())
        validTransaction.update_location(
            self.locations_generator.generate_next_location(validTransaction.card_id))

        result.append((self.get_suspicious_waiting_time(), validTransaction))

        invalidTransaction = self.get_result(self.get_value())
        invalidTransaction.user_id = validTransaction.user_id
        invalidTransaction.card_id = validTransaction.card_id

        invalidTransaction.location = self.locations_generator.generate_next_suspicious_location(
            invalidTransaction.card_id)

        result.append((self.get_suspicious_waiting_time(), invalidTransaction))

        return result
