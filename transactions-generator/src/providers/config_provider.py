from os import getenv


class ConfigProvider:
    def __init__(self):
        self.CARDS_NUMBER = int(getenv('CARDS_NUMBER'))
        self.MAX_CARDS_PER_USER = int(getenv("MAX_CARDS_PER_USER"))
        self.MEAN_CARDS_PER_USER = int(getenv("MEAN_CARDS_PER_USER"))
        self.STD_DEV_CARDS_PER_USER = int(getenv("STD_DEV_CARDS_PER_USER"))
        self.USERS_NUMBER = self.CARDS_NUMBER/self.MAX_CARDS_PER_USER
        self.KAFKA_TOPIC = getenv("KAFKA_TOPIC")
        self.KAFKA_BOOTSTRAP_SERVER = getenv("KAFKA_BOOTSTRAP_SERVER")
        self.IS_DEVELOPMENT = bool(getenv("DEVELOPMENT") == "True")
        self.NUMBER_OF_EVENTS = int(getenv("NUMBER_OF_EVENTS")) if getenv(
            "NUMBER_OF_EVENTS") != None else None
        self.MIN_FOUNDS = float(getenv("MIN_FOUNDS"))
        self.MAX_FOUNDS = float(getenv("MAX_FOUNDS"))
        self.MIN_FOUND_TO_REUSE_USER = float(getenv("MIN_FOUND_TO_REUSE_USER"))

        if self.CARDS_NUMBER is None or self.USERS_NUMBER is None or self.MAX_CARDS_PER_USER is None:
            raise Exception("Provide all required env variables!")
