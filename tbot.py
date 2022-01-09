import telebot
from pars import span, ahref
import priceSG
import utils
from baze import TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['news'])  # Просмотр новостей, парсинг новостей
def send_welcome(message):
    bot.send_message(message.chat.id, 'Новости с www.yandex.ru')

    for i in range(len(span)):
        atext = ahref[i].get('href')
        text = str(span[i].getText()) + '. [подробнее...](' + str(atext) + ')'
        bot.send_message(message.chat.id,  text, parse_mode='Markdown', disable_web_page_preview=True)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if {message.from_user.first_name}:
        bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}")
    else:
        bot.send_message(message.chat.id, f"Привет, {message.chat.username}")
    bot.send_message(message.chat.id, "Для работы с ботом используйте следующие команды:")
    bot.send_message(message.chat.id, "Последние новости: /news")
    bot.send_message(message.chat.id, "Цены на ТШ с сайта Станкограда: /price")
    bot.send_message(message.chat.id,
                     "Конвертация валют: введите 3-х буквенное значение валюьы (USD, RUB и т.д.)\n"
                     "<конвертированная валюта> <количество> <в какую валюту конвертировать>")


@bot.message_handler(commands=['help', ])
def send_welcome(message):
    bot.send_message(message.chat.id, "Цены с сайта Станкограда: /price\n"
                                      "\n"
                                      "Последние новости: /news\n"
                                      '\n'
                                      "Конвертация валют: введите 3-х буквенное значение валюты (USD, RUB и т.д.)"
                                      "\n \
<конвертированная валюта> <количество> <в какую валюту конвертировать>")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD1')


@bot.message_handler(commands=['price', ])  # Парсинг сайта
def values(message: telebot.types.Message):
    tex = priceSG.price()
    text = 'Цены на сайте Станкограда на станки точильно-шлифовальные:'
    for key in tex:

        text = '\n'.join((text, key + ' - ' + tex[key],))
        text = text.replace('Станок точильно-шлифовальный ', '')
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])  # Работа с API
def convert(message: telebot.types.Message):
    try:
        text = message.text.split()
        if len(text) != 3:
            raise utils.ConvertExcept('Не верная длина команды.')

        quet, amaund, base = text
        itog = utils.Criptoconv.convert(quet, amaund, base)
    except utils.ConvertExcept as e:
        bot.reply_to(message, f"Ошибка пользователя. \n{e}")
    except Exception as e:
        bot.reply_to(message, f"Бот не справился.... \nКод ошибки:{e}")
    else:
        bot.reply_to(message, f'{amaund} {quet} = {itog} {base}')


bot.polling(none_stop=True)
