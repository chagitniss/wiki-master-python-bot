import logging

import model
import settings
import secret_settings

from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ChatAction

TOKEN = secret_settings.BOT_TOKEN
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(
    format='[%(levelname)s %(asctime)s %(module)s:%(lineno)d] %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)

game = model.Game()


def send_gif(bot, image_url, chat_id):
    bot.sendChatAction(chat_id=chat_id, action=ChatAction.UPLOAD_PHOTO)
    bot.sendDocument(chat_id=chat_id, document=image_url)


def start(bot, update):
    chat_id = update.message.chat_id
    logger.info(f"> Start chat #{chat_id}")

    game.add_user(chat_id)
    page_title = game.get_page_title(chat_id)

    keyboard = [[InlineKeyboardButton("Yes", callback_data='2'), InlineKeyboardButton("No", callback_data='3')]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(chat_id=chat_id, text=f"Welcome To The Wiki Master Bot!\n")

    bot.send_message(chat_id=chat_id,
                     text=f"Check out how much you know relative to wikipedia, the site that knows everything.\n")

    bot.send_message(chat_id=chat_id, text=f"Let's start!\nHave you heard of '{page_title}'?",
                     reply_markup=reply_markup)


def respond(bot, update):
    chat_id = update.message.chat_id
    text = update.message.text
    logger.info(f"= Got on chat #{chat_id}: {text!r}")

    message = game.test_word(text, chat_id)

    if 'win' in message or 'fail' in message:
        keyboard = [[InlineKeyboardButton("New Game", callback_data='1'),
                    InlineKeyboardButton("Page Summary", callback_data='4')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        send_gif(bot,message[message.index('url') + 3:], chat_id )
        bot.send_message(chat_id=chat_id, text=message[:message.index('url')], reply_markup=reply_markup)

    else:
        bot.send_message(chat_id=chat_id, text=message)


def button(bot, update):
    query = update.callback_query
    chat_id = query.message.chat_id

    if query.data == '1':  # new game
        logger.info(f"= Got on chat #{chat_id}: pressed New Game button")

        game.add_user(chat_id)
        page_title = game.get_page_title(chat_id)

        keyboard = [[InlineKeyboardButton("Yes", callback_data='2'), InlineKeyboardButton("No", callback_data='3')]]
        reply_markup = InlineKeyboardMarkup(keyboard)

        bot.send_message(chat_id=chat_id, text=f"Let's start!\n"
                         f"Have you heard of '{page_title}'?", reply_markup=reply_markup)

    elif query.data == '2':  # starting the guessing process
        logger.info(f"= Got on chat #{chat_id}: pressed Yes button")
        message = game.test_button_click('yes', chat_id)

        if 'your turn' in message:
            bot.send_message(chat_id=chat_id, text="great!\nI just checked what Wikipedia knows about it.\n")
        bot.send_message(chat_id=chat_id, text=message)

    elif query.data == '3':  # Another title is suggested
        logger.info(f"= Got on chat #{chat_id}: pressed No button")
        message = game.test_button_click('no', chat_id)

        if 'invalid' in message:
            bot.send_message(chat_id=chat_id, text=message)

        else:
            keyboard = [[InlineKeyboardButton("Yes", callback_data='2'), InlineKeyboardButton("No", callback_data='3')]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            bot.send_message(chat_id=chat_id, text=message, reply_markup=reply_markup)

    elif query.data == '4':
        keyboard = [[InlineKeyboardButton("New Game", callback_data='1')]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        summary = game.get_info(chat_id)
        bot.send_message(chat_id=chat_id, text=summary, reply_markup=reply_markup)


def help(bot, update):
    chat_id = update.message.chat_id
    keyboard = [[InlineKeyboardButton("New Game", callback_data='1')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    bot.send_message(chat_id=chat_id, text=settings.HELP_MESSAGE, reply_markup=reply_markup)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text, respond)
dispatcher.add_handler(echo_handler)

help_handler = CommandHandler('help', help)
dispatcher.add_handler(help_handler)

updater.dispatcher.add_handler(CallbackQueryHandler(button))
logger.info("Start polling")
updater.start_polling()



