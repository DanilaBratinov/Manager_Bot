import telebot
import commands
import database
import messages

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
# token = '6526866415:AAGgaKPE25fw4DHvD0MBzENf39BYRev3QcE'
bot = telebot.TeleBot(token)

def get_db(message):
    db = (f"id{message.from_user.id}")
    return db

try:
    database.connection()

    @bot.message_handler(commands=['start'])
    def start_message(message):
        db = (f"id{message.from_user.id}")
        # database.create_table(db)
        # commands.start(message)
        # bot.send_message(message.chat.id, "asd")
        bot.send_message(message.chat.id, db)


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        db = (f"id{message.from_user.id}")
        chatID = message.chat.id
        match message.text:
            case "Посмотреть задачи":
                bot.send_message(chatID, database.show_tasks(db))

            case "Очистить список":
                database.clear_db(get_db)
                bot.send_message(chatID, "Список очищен")

            case "Главная":
                bot.send_message(chatID, messages.hello(message))


except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
