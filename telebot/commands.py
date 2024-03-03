import telebot
import messages
import web
from telebot import types

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)


def start(message):
    chatID = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Добавить задачу')
    item2 = types.KeyboardButton('Посмотреть задачи')
    item3 = types.KeyboardButton('Очистить список')
    item4 = types.KeyboardButton('Главная')

    markup.add(item1, item2, item3, item4)

    bot.send_message(chatID, messages.hello_message)