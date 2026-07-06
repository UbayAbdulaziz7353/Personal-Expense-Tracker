from abc import ABC, abstractmethod
from api.exchange_api import ExchangeRateAPI

class ConversionStrategy(ABC):
    @abstractmethod
    def convert(self, amount, currency):
        pass

class LiveRateStrategy(ConversionStrategy):
    def __init__(self):
        self.api = ExchangeRateAPI()

    def convert(self, amount, currency):
        rate = self.api.get_rate(currency)
        return amount * rate

class CurrencyConverter:
    def __init__(self, strategy):
        self.strategy = strategy

    def convert(self, amount, currency):
        return self.strategy.convert(amount, currency)
