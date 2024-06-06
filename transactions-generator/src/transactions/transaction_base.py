from typing import Tuple
from models import TransactionResult, TransactionResultBase, User
from providers import ScenarioProvider, IdProvider
from generators.locations_generator import LocationsGenerator
import numpy as np


class TransactionBase:
    scenario: ScenarioProvider
    locations_generator: LocationsGenerator
    id_provider: IdProvider
    user: User

    TYPE: str = None

    def __init__(self, locations_generator: LocationsGenerator, id_provider: IdProvider, scenario: ScenarioProvider, user: User):
        self.scenario = scenario
        self.user = user
        self.id_provider = id_provider
        self.locations_generator = locations_generator

    def generate(self) -> list[Tuple[float, TransactionResult]]:
        pass

    def get_result(self, value: float) -> TransactionResult:
        pass

    def update_limit(self, value: float) -> float:
        self.user.limit = round(max(0, (self.user.limit-value)), 2)

    def get_value(self) -> float:
        value = round(np.random.uniform(
            self.scenario.MIN_VALUE_AMOUNT, self.scenario.LIMIT_PERCENT_TRESHOLD*self.user.limit), 2)

        return value

    def get_result_base(self, value) -> TransactionResultBase:
        card_id = np.random.choice(self.user.cards_ids)
        tran_id = self.id_provider.get_next()

        self.update_limit(value)

        return TransactionResultBase(tran_id, card_id, user_id=self.user.user_id, value=value, type=self.TYPE, limit=self.user.limit)

    def get_valid_waiting_time(self):
        return np.random.uniform(self.scenario.ORDINARY_TRAN_TIME_RANGE._from, self.scenario.ORDINARY_TRAN_TIME_RANGE._to)
