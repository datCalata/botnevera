from telegram.ext import Updater
from telegram.ext import CommandHandler
import logging
from telegram import Bot
import bot_telegram_callback


updater = Updater(token='460631781:AAEzUbO50_7B7zS3qj-WM89s9pi_9jXdRcU')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level = logging.INFO)

bot = Bot(token='460631781:AAEzUbO50_7B7zS3qj-WM89s9pi_9jXdRcU')

start_handler = CommandHandler('start',bot_telegram_callback.start) #Callback
dispatcher.add_handler(start_handler)

updater.start_polling()

