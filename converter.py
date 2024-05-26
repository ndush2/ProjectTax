import requests

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.exchange_rates = {}

    @property
    def kes_rate(self):
        self._fetch_exchange_rates_if_needed()
        return self.exchange_rates.get('KES', None)

    def convert_usd_to_kes(self, usd_amount):
        kes_rate = self.kes_rate
        if kes_rate is None:
            raise ValueError("KES exchange rate not found in the API response")
        return usd_amount * kes_rate

    def _fetch_exchange_rates_if_needed(self):
        if not self.exchange_rates:
            api_url = f'https://openexchangerates.org/api/latest.json?app_id={self.api_key}'
            response = requests.get(api_url)
            response.raise_for_status()
            self.exchange_rates = response.json()['rates']