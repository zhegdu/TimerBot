from telegram.ext import CommandHandler, Filters, MessageHandler, Updater
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN_BOT = os.getenv('TOKEN_BOT')


updater = Updater(token=TOKEN_BOT)

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id,text='Привет, я TimerBot!')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    context.bot.send_message(
        chat_id=chat.id,
        text='Спасибо, что вы включили меня, {}!'.format(name)
        )

updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))

updater.start_polling()
updater.idle()