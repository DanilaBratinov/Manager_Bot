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
        database.create_table(message)
        commands.start(message)

    @bot.message_handler(content_types=['text'])
    def send_message(message):
        chatID = message.chat.id
        db = (f"id{message.from_user.id}")

        match message.text:
            # case "Добавить задачу":
                # add_task_one(message)

            case "Посмотреть задачи":
                bot.send_message(chatID, database.show_tasks(db))
            
            # case "Очистить список":
            #     with connection.cursor() as cursor:
            #         cursor.execute(f"DELETE FROM {str(db)};")
            #         connection.commit()
            #         bot.send_message(chatID, "Список очищен!")

        


except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
