import json


class Serializable:
    def to_dict(self) -> dict:
        return {}


def serializer(instance: Serializable):
    return json.dumps(instance, default=str).encode('utf-8')
