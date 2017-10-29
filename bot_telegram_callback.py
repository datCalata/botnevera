import telegram.user


#Callback Functions
def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")
    usuario = update.message.from_user
    bot.send_message(chat_id=update.message.chat_id,text="usuario {}, id {}".format(usuario['username'], usuario['id']))
