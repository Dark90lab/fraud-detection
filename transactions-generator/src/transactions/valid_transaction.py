from typing import Tuple
from .transaction_base import TransactionBase
from models import TransactionResult
import numpy as np


class ValidTransaction(TransactionBase):

    TYPE = 'N'

    def generate(self) -> list[Tuple[float, TransactionResult]]:
        return [(self.get_valid_waiting_time(), self.get_result(self.get_value()))]

    def get_value(self) -> float:
        return np.random.uniform(self.scenario.MIN_VALUE_AMOUNT, self.scenario.LARGE_VALUE_AMOUNT)

    def get_result(self, value: float) -> TransactionResult:
        tran_base = super().get_result_base(value)

        location = self.locations_generator.generate_next_location(
            tran_base.card_id)

        return TransactionResult.fromBase(tran_base).update_location(location)
