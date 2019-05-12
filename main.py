from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


token = u'883808686:AAGr0NIkmfUDBKXs6Y3cExoi3CKxJsPtILE'

# check for new messages from API (polling)
updater = Updater(token=token)

# allow to register handler
dispatcher = updater.dispatcher

# define a command callback function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello, welcome do LimaBOT")

# create a command handler
start_handler = CommandHandler("start", start)

# add command handler to dispatcher
dispatcher.add_handler(start_handler)

def echo(bot, update):
    print(update.message.text)
    bot.send_message(chat_id=update.message.chat_id, text=update.message.text.upper())

# create a text message handler
echo_handler = MessageHandler(Filters.text, echo)

# add message handler to dispatcher
dispatcher.add_handler(echo_handler)

#start pooling
updater.start_polling()