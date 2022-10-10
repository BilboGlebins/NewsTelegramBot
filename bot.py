import telebot
import configuration as conf


bot = telebot.TeleBot(conf.botToken)


@bot.message_handler(commands=['start'])


def start(message):
    bot.send_message(message.chat.id, conf.textStart)






bot.polling(none_stop=True)
