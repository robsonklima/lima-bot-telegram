# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import time


token = u'883808686:AAE4EmhBTO8TeT7O5poI5WyiPUEa2WaWNd8'
updater = Updater(token=token)
dispatcher = updater.dispatcher


def start(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Olá {first_name}!".format(first_name=update.message.chat.first_name))
    except Exception as ex:
        print(ex)

def echo(bot, update):
    try:
        bot.send_message(chat_id=update.message.chat_id, text="Olá {first_name}!".format(first_name=update.message.chat.first_name))

        print(update)
    except Exception as ex:
        print(ex)


start_handler = CommandHandler("start", start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
updater.start_polling()