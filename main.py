import telebot
from config import keys, TOKEN
from utils import ConvertionException, CriptoConvecter

bot = telebot.TeleBot(TOKEN)

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
    try:
        val = message.text.split(' ')

        if len(val) != 3:
            raise ConvertionException("Лишние данные или недостаточно данных")

        quote, base, amount = val
        total = CriptoConvecter.convector(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя. \n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду. \n{e}")
    else:
        text = f'Цена {amount} {quote} в {base} -  {total}'
        bot.send_message(message.chat.id, text)


bot.polling()
