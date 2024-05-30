from .location import Location
from .transaction_result_base import TransactionResultBase


class TransactionResult(TransactionResultBase):
    def __init__(self, id: int, card_id: int, user_id: int, location: Location, value: float, type: str) -> None:
        super().__init__(id, card_id, user_id, value, type)
        self.location = location

    @classmethod
    def fromBase(self, base: TransactionResultBase):
        return TransactionResult(id=base.id, card_id=base.card_id, user_id=base.user_id, location=None, value=base.value, type=base.type)

    def update_location(self, location: Location):
        self.location = location
        return self

    def to_dict(self):
        return {
            'id': int(self.id),
            'type': self.type,
            'user_id': int(self.user_id),
            'card_id': int(self.card_id),
            'value': self.value,
            'timestamp': self.timestamp,
            'location': self.location.to_dict()
        }
