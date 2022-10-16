import telebot
import re
from telebot import types

import configuration as conf
import scraping.ria_news as ria_news

amt_news = conf.amt_news + 1

bot = telebot.TeleBot(conf.botToken)
button_rianews = types.KeyboardButton("РИА")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, conf.textStart)


@bot.message_handler(commands=['from_source'])
def from_source(message):
    markup_source = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_source.add(button_rianews)
    message_source = bot.send_message(message.chat.id, conf.testSourse, reply_markup=markup_source)
    bot.register_next_step_handler(message_source, output_news)


def output_news(message):
    if message.text == 'РИА':
        for i in range(1, amt_news):
            bot.send_message(message.chat.id, ria_news.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['update_n'])
def from_source(message):
    message_update = bot.send_message(message.chat.id, conf.textUpdate)
    bot.register_next_step_handler(message_update, update_amt)


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


@bot.message_handler(commands=['subscribe'])
def from_source(message):
    markup_subscribe = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_subscribe.add(button_rianews)
    message_subscribe = bot.send_message(message.chat.id, conf.testSubscribe, reply_markup=markup_subscribe)
    bot.register_next_step_handler(message_subscribe, sub_news)


def sub_news(message):
    if message.text == 'РИА':
        bot.send_message(message.chat.id, conf.testSubscribeDone)


bot.polling(none_stop=True)
