import telebot
from telebot import types

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

def chatID(message):
    chatID = message.chat.id
    return chatID
