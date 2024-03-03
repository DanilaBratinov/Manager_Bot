import telebot
import pymysql
import commands
import database
from config import host, user, password, db_name

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

try:
    database.connection()

    @bot.message_handler(commands=['start'])
    def start_message(message):
        database.create_table(database.connection, message)
        commands.start(message)
        


except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
