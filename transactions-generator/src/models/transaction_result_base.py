from datetime import datetime
from utils import Serializable


class TransactionResultBase(Serializable):
    def __init__(self, id: int, card_id: int, user_id: int, value: float, type: str) -> None:
        self.id = id
        self.card_id = card_id
        self.user_id = user_id
        self.value = value
        self.timestamp = datetime.now().timestamp()
        self.type = type

    def update_timestamp(self, timestamp):
        self.timestamp = timestamp if timestamp is not None else datetime.now().timestamp()
        return self
