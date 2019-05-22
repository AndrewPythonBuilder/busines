import logging
import constants, base_w
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Contact, KeyboardButton, ChatMember, ChatAction
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
updater = Updater(token=constants.token)
dispatcher = updater.dispatcher

def start(bot, update):
    message = update.message
    botton = [[InlineKeyboardButton('lol', callback_data='lol'), InlineKeyboardButton('kek', callback_data='kek')]]
    keyboard = InlineKeyboardMarkup(botton)
    bot.send_message('@LA_Channelove', 'Топ', reply_markup=keyboard)

def button(bot, update):
    query = update.callback_query
    if str(query.data) == '👍':
        print(query)
    else:
        bot.send_action(query.from_user.id, 'https://t.me/LA_schedule_Bot')

start_handler = MessageHandler(Filters.all, start)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling(timeout=5, clean=True)