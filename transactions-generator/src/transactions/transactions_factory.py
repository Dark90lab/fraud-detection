from typing import Dict, Type
from models import FraudType
from providers import ScenarioProvider
from .transaction_base import TransactionBase
from .value_treshold_fraud_transaction import ValueTresholdFraudTransaction
from .valid_transaction import ValidTransaction
import numpy as np


class TransactionsFactory:
    frauds_transactions_map: Dict[FraudType, Type[TransactionBase]] = {
        FraudType.VALUE_TRESHOLD: ValueTresholdFraudTransaction,
        FraudType.NONE: ValidTransaction
    }

    def __init__(self, scenario_provider: ScenarioProvider) -> None:
        self.scenario = scenario_provider

    def get_transaction_factory(self) -> Type[TransactionBase]:
        rand_number = np.random.uniform(0, 1)
        cumulative_probability = 0

        sorted_entries = sorted(
            self.scenario.frauds_probabilities.items(), key=lambda x: x[1], reverse=True)

        for fraud_type, probability in sorted_entries:
            cumulative_probability += probability

            if rand_number < cumulative_probability:
                transaction = self.frauds_transactions_map[fraud_type]

                if transaction is None:
                    raise Exception(
                        f"There is no defined event class for FraudType {fraud_type}")

                return transaction
