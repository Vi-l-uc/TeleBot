import requests
import json


class ConvertExcept(Exception):
    pass


class Criptoconv:
    @staticmethod
    def convert(quet: str, amaund: str, base: str):

        if quet == base:
            ConvertExcept('Одинаковые параметры')

        if amaund.find(',') != -1:
            amaund = amaund.replace(",", '.')

        try:
            amaund = float(amaund)
        except ValueError:
            raise ConvertExcept(f"Не удалость обработать количество<{amaund}>")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quet}&tsyms={base}')
        itog = round(float(json.loads(r.content)[base])*float(amaund), 2)
        try:
            itog = float(itog)
        except ValueError:
            raise ConvertExcept(f'В базе данных не найден код валюты {quet} или {base}')

        return itog
