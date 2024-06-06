from .transaction_base import TransactionBase
from typing import Tuple
from models import TransactionResult
import numpy as np


class ValueTresholdFraudTransaction(TransactionBase):
    TYPE = 'VT'

    def get_result(self, value: float) -> TransactionResult:
        tran_base = super().get_result_base(value)
        location = self.locations_generator.generate_next_location(
            tran_base.card_id)

        return TransactionResult.fromBase(tran_base).update_location(location)

    def get_suspicious_waiting_time(self) -> float:
        return np.random.uniform(self.scenario.VALUE_TRESHOLD_FRAUDS_TIME_RANGE._from, self.scenario.VALUE_TRESHOLD_FRAUDS_TIME_RANGE._to)

    def generate(self) -> list[Tuple[float, TransactionResult]]:
        result: list[Tuple[float, TransactionResult]] = list()

        small_amount_transaction = self.get_result(
            round(np.random.uniform(0.01, self.scenario.MIN_VALUE_AMOUNT), 2))

        result.append((self.get_suspicious_waiting_time(),
                      small_amount_transaction))

        large_amount_transaction = self.get_result(round(
            np.random.uniform(self.scenario.LIMIT_PERCENT_TRESHOLD*self.user.limit, self.user.limit), 2)
        )

        result.append((self.get_suspicious_waiting_time(),
                      large_amount_transaction))

        return result
