import telebot
import pymysql
import commands
import database
from config import host, user, password, db_name

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )

    @bot.message_handler(commands=['start'])
    def start_message(message):
        database.create_table(connection)
        commands.start(message)
        


except Exception as ex:

    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
