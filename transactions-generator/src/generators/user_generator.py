from providers import ConfigProvider
import numpy as np
import random
from .base_generator import BaseGenerator
from typing import Dict
from models import User


class UserGenerator(BaseGenerator):
    def __init__(self, config_provider: ConfigProvider):
        super().__init__(config_provider)
        self.available_cards = set(range(1, self.config.CARDS_NUMBER+1))
        self.generated_user_ids: Dict[int, list[int]] = dict()

    def get_number_of_user_cards(self):
        num_cards_user = int(np.random.normal(
            self.config.MEAN_CARDS_PER_USER, self.config.STD_DEV_CARDS_PER_USER))

        return max(1, min(num_cards_user, self.config.MAX_CARDS_PER_USER))

    def get_user_data(self) -> User:
        user_id = random.randint(1, self.config.USERS_NUMBER)

        if self.generated_user_ids.get(user_id) is None:
            num_cards_user = self.get_number_of_user_cards()
            cards_assigned = random.sample(
                self.available_cards, num_cards_user)

            self.available_cards -= set(cards_assigned)
            self.generated_user_ids[user_id] = list(cards_assigned)

        return User(user_id, self.generated_user_ids[user_id])
