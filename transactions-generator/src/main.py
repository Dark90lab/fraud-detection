from dotenv import load_dotenv
from generators import TransactionsGenerator
from providers import ScenarioProvider, ConfigProvider
from kafka import KafkaProducer
from utils import serializer

if __name__ == "__main__":
    load_dotenv()

    scenario_provider = ScenarioProvider()
    config_provider = ConfigProvider()

    producer = KafkaProducer(bootstrap_servers=[config_provider.KAFKA_BOOTSTRAP_SERVER],
                             value_serializer=serializer)

    TransactionsGenerator(config_provider, scenario_provider, producer).run()
