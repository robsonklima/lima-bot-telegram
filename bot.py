import telegram


token = '883808686:AAHev-RK_oBfpk-juuTf64YfR7MlUJ7eauo'
bot = telegram.Bot(token=token)


#print(bot.get_me())
messages = bot.get_updates()

for msg in messages:
    print(msg.message.text)