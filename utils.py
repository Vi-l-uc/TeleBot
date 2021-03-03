import requests
import json
from config import keys


class ConvertionException(Exception):
    pass


class CriptoConvecter:
    @staticmethod
    def convector(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f"Невозможно перевести {base} в {base}")

        try:
            quote_tic = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_tic = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        if amount.find(',') != -1:
            raise ConvertionException(f'Замените запятую на точку в {amount}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_tic}&tsyms={base_tic}")
        total = round(float(json.loads(r.content)[keys[base]])*float(amount), 2)

        return total
