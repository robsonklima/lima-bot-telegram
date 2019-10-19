# -*- coding: utf-8 -*-
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = u'883808686:AAG3B4Yw7CAo5WWXAcPjp5o67mQ3-Te_u3M'
bot = telegram.Bot(token=token)

bot.send_message(chat_id=649566006, text="Enviando localização...")
bot.send_location(chat_id=649566006)