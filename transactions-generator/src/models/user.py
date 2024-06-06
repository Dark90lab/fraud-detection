from typing import Dict


class User:
    def __init__(self, user_id: int, cards_ids: Dict[int, list[int]], limit: float) -> None:
        self.user_id = user_id
        self.cards_ids = cards_ids
        self.limit = limit
