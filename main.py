import telebot
import requests
import json

TOKEN = '1509594923:AAFDUTQCO7aTxcBLOgHJ7mWiQBIJaKYXIBc'

bot = telebot.TeleBot(TOKEN)

keys = {"доллар": "USD",
        "евро": "EUR",
        "рубль": "RUB",
}


class ConvertionException(Exception):
    pass

class CriptoConvecter:
    @staticmethod
    def convector( quote: str, base: str, amount: str):



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

        #try:
        #    amount = float(amount)
        #except ValueError:
        #    raise ConvertionException(f'Не удалось обработать {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_tic}&tsyms={base_tic}")
        total = round(float(json.loads(r.content)[keys[base]])*float(amount), 2)

        return total


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    start_txt = "\nЧто бы начать работу введите команду боту в следующем формате: \n" \
            "<имя валюты> <в какаю валюту перевести> <количество>"
    if message.chat.username:
        bot.send_message(message.chat.id, f"Привет, {message.chat.username} {message.from_user.first_name}")
    else:
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    bot.send_message(message.chat.id, start_txt)
    bot.send_message(message.chat.id, "Узнать доступные валюты: /values")


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def values(message: telebot.types.Message):
    val = message.text.split(' ')

    if len(val) != 3:
        raise ConvertionException("Лишние данные или недостаточно данных")

    quote, base, amount = val
    total = CriptoConvecter.convector(quote, base, amount)
    text = f'Цена {amount} {quote} в {base} -  {total}'
    bot.send_message(message.chat.id, text)


bot.polling()
