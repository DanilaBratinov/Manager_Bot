import telebot
import commands
import database
import messages

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

def get_db(message):
    db = (f"id{message.from_user.id}")
    return db

try:
    database.connection

    @bot.message_handler(commands=['start'])
    def start_message(message):
        db = (f"id{message.from_user.id}")
        database.create_table(db)
        commands.start(message)


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        db = (f"id{message.from_user.id}")
        chatID = message.chat.id
        match message.text:
            case "Добавить задачу":
                database.add_task(bot, message)
                bot.register_next_step_handler(message, database.add_task_name(bot, message))
                bot.register_next_step_handler(message, database.add_task_time(bot, message))
                bot.register_next_step_handler(message, database.add_task_date(bot, message))




            case "Посмотреть задачи":
                # bot.send_message(chatID, database.show_tasks(db))
                database.show_tasks(bot, message)

            case "Очистить список":
                database.clear_db(get_db, bot, message)
                # bot.send_message(chatID, "Список очищен")

            case "Главная":
                bot.send_message(chatID, messages.hello(message))


except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
