import telebot
import configuration as conf
import scraping.ria_news as ria_news
amt_news = conf.amt_news + 1

bot = telebot.TeleBot(conf.botToken)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, conf.textStart)


@bot.message_handler(commands=['from_source'])
def from_source(message):
    for i in range(1, amt_news):
        bot.send_message(message.chat.id, ria_news.scraping_news(i))


bot.polling(none_stop=True)
