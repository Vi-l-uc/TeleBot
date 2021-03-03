import telebot
import requests
import json
TOKEN = '1509594923:AAFDUTQCO7aTxcBLOgHJ7mWiQBIJaKYXIBc'
bot = telebot.TeleBot(TOKEN)

keys = {"доллар": "USD",
        "евро": "EUR",
        "рубль": "RUB",
}


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


@bot.message_handler(convent_types=['text'])
def values(message: telebot.types.Message):
    quote, base, amount = message.text.split(' ')
    r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}")
    total = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} -  {total}'
    bot.send_message(message.chat.id, text)


bot.polling()
