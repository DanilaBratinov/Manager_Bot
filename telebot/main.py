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
    database.connection()

    @bot.message_handler(commands=['start'])
    def start_message(message):
        database.create_table(get_db)
        commands.start(message)

    @bot.message_handler(content_types=['text'])
    def send_message(message):
        chatID = message.chat.id
        match message.text:
            case "Посмотреть задачи":
                bot.send_message(chatID, database.show_tasks(get_db))

            case "Очистить список":
                database.clear_db(get_db)
                bot.send_message(chatID, "Список очищен")

            case "Главная":
                bot.send_message(chatID, messages.hello)


        


except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
