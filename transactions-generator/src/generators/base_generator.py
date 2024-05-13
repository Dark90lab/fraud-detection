from providers import ConfigProvider


class BaseGenerator:
    config: ConfigProvider

    def __init__(self, config_provider: ConfigProvider) -> None:
        self.config = config_provider
