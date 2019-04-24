from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
import logging
from telegram import Bot
import bot_telegram_callback
import pathlib

current_dir = pathlib.Path(__file__).parent
current_file = pathlib.Path(__file__)

print(current_dir)
print(current_file)


updater = Updater(token='460631781:AAEzUbO50_7B7zS3qj-WM89s9pi_9jXdRcU')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

bot = Bot(token='460631781:AAEzUbO50_7B7zS3qj-WM89s9pi_9jXdRcU')

start_handler = CommandHandler('start',bot_telegram_callback.start) #Callback
comprar_handler = CommandHandler('comprar',bot_telegram_callback.comprar,pass_user_data=True)
mete_dinero_handler = CommandHandler('metedinero',bot_telegram_callback.mete_dinero,pass_args=True)
dinero_handler = CommandHandler('dinero',bot_telegram_callback.dinero)
comprar_query_handler = CallbackQueryHandler(bot_telegram_callback.button,pass_user_data=True)
ayuda_handler = CommandHandler('ayuda',bot_telegram_callback.ayuda)
dispatcher.add_handler(comprar_query_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(comprar_handler)
dispatcher.add_handler(mete_dinero_handler)
dispatcher.add_handler(dinero_handler)
dispatcher.add_handler(ayuda_handler)

updater.start_polling()

