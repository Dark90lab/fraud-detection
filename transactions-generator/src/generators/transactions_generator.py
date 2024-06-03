from providers import ConfigProvider, ScenarioProvider, IdProvider
import time
from .user_generator import UserGenerator
from .base_generator import BaseGenerator
from .locations_generator import LocationsGenerator
from transactions import TransactionsFactory
from utils import serializer
from kafka import KafkaProducer

# TODO: make scenario and config providers as singleton


class TransactionsGenerator(BaseGenerator):
    def __init__(self, config_provider: ConfigProvider, scenario_provider: ScenarioProvider, producer: KafkaProducer):
        super().__init__(config_provider)
        self.user_generator = UserGenerator(self.config)
        self.scenario = scenario_provider
        self.transactions_factory = TransactionsFactory(self.scenario)
        self.locations_generator = LocationsGenerator(self.config)
        self.id_provider = IdProvider()
        self.producer = producer

    def generate_transaction(self):
        pass

    def run(self):
        while True:
            user = self.user_generator.get_user_data()
            transaction_factory = self.transactions_factory.get_transaction_factory()

            print(
                f"User ID {user.user_id} assigned cards {user.cards_ids}")

            transactions = transaction_factory(
                self.locations_generator, self.id_provider, self.scenario, user).generate()

            for (timeout, transaction) in transactions:

                print(serializer(transaction.to_dict()))

                if self.config.IS_DEVELOPMENT == False:
                    self.producer.send(self.config.KAFKA_TOPIC,
                                       transaction.to_dict())

                time.sleep(timeout)
