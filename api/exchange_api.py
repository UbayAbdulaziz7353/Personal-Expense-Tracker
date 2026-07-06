import requests

class ExchangeRateAPI:
    BASE_URL = "https://open.er-api.com/v6/latest/USD"

    def get_rate(self, currency: str):
        response = requests.get(self.BASE_URL)
        data = response.json()

        return data["rates"][currency.upper()]
