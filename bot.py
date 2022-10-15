import telebot
import re
from telebot import types

import configuration as conf
import scraping.ria_news as ria_news

amt_news = conf.amt_news + 1

bot = telebot.TeleBot(conf.botToken)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, conf.textStart)


@bot.message_handler(commands=['from_source'])
def from_source(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_rianews = types.KeyboardButton("РИА")
    markup.add(button_rianews)
    bot.send_message(message.chat.id, conf.testSourse, reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def output_news(message):
        if message.text == 'РИА':
            for i in range(1, amt_news):
                bot.send_message(message.chat.id, ria_news.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['update_n'])
def from_source(message):
    bot.send_message(message.chat.id, conf.textUpdate)

    @bot.message_handler(content_types=['text'])
    def update_amt(message):
        if re.findall(r'\d[0-9]', message.text):
            if int(message.text) <= 20:
                bot.send_message(message.chat.id, conf.textPassUpdate)
                global amt_news
                amt_news = int(message.text)
                return amt_news
            else:
                bot.send_message(message.chat.id, conf.textErrorUpdate)
        else:
            bot.send_message(message.chat.id, conf.textErrorUpdate)


bot.polling(none_stop=True)
