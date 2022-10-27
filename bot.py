import telebot
import re
from telebot import types

import configuration as conf
import scraping.ria_news as ria_news
import scraping.rbk as rbk
import scraping.kommersant as kommersant
import scraping.sport_ru as sport_ru

amt_news = conf.amt_news + 1

bot = telebot.TeleBot(conf.botToken)
button_rianews = types.KeyboardButton('РИА')
button_rbc = types.KeyboardButton('РБК')
button_kommersant = types.KeyboardButton('Ъ')
button_sportru = types.KeyboardButton('S')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, conf.textStart)


@bot.message_handler(commands=['from_source'])
def from_source(message):
    markup_source = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup_source.add(button_rianews, button_rbc, button_kommersant, button_sportru)
    message_source = bot.send_message(message.chat.id, conf.testSourse, reply_markup=markup_source)
    bot.register_next_step_handler(message_source, output_news)


def output_news(message):
    if message.text == 'РИА':
        for i in range(1, amt_news):
            bot.send_message(message.chat.id, ria_news.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'РБК':
        for i in range(1, amt_news):
            bot.send_message(message.chat.id, rbk.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'Ъ':
        for i in range(1, amt_news):
            bot.send_message(message.chat.id, kommersant.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())
    if message.text == 'S':
        for i in range(1, amt_news):
            bot.send_message(message.chat.id, sport_ru.scraping_news(i), reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['update_n'])
def from_source(message):
    message_update = bot.send_message(message.chat.id, conf.textUpdate)
    bot.register_next_step_handler(message_update, update_amt)


def update_amt(message):
    if re.findall(r'[0-9]', message.text):
        if int(message.text) <= 10:
            bot.send_message(message.chat.id, conf.textPassUpdate)
            global amt_news
            amt_news = int(message.text) + 1
            return amt_news
        else:
            bot.send_message(message.chat.id, conf.textErrorUpdate)
    else:
        bot.send_message(message.chat.id, conf.textErrorUpdate)


@bot.message_handler(commands=['subscribe'])
def from_source(message):
    bot.send_message(message.chat.id, 'in the process')
    #markup_subscribe = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #markup_subscribe.add(button_rianews, button_rbc, button_kommersant)
    #message_subscribe = bot.send_message(message.chat.id, conf.testSubscribe, reply_markup=markup_subscribe)
    #bot.register_next_step_handler(message_subscribe, sub_news)

#def sub_news(message):
#    if message.text == 'РИА':
#        bot.send_message(message.chat.id, conf.testSubscribeDone)
#    if message.text == 'РБК':
#        bot.send_message(message.chat.id, conf.testSubscribeDone)
#    if message.text == 'Ъ':
#        bot.send_message(message.chat.id, conf.testSubscribeDone)


bot.polling(none_stop=True)
