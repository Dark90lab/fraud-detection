from .transaction_base import TransactionBase
from typing import Tuple
from models import TransactionResult
import numpy as np


class SuspiciousLocationFruadTransaction(TransactionBase):
    TYPE = 'SL'

    def get_result(self, value: float) -> TransactionResult:
        tran_base = super().get_result_base(value)

        return TransactionResult.fromBase(tran_base)

    def generate(self) -> list[Tuple[float, TransactionResult]]:
        result: list[Tuple[float, TransactionResult]] = list()

        outlier_result = self.get_result(self.get_value())

        outlier_result.update_location(self.locations_generator.generate_outlier_location(
            outlier_result.card_id))

        result.append((self.get_valid_waiting_time(), outlier_result))

        return result
