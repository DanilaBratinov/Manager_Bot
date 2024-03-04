import commands
import database
import messages
bot = commands.bot

def get_db(message):
    db = (f"id{message.from_user.id}")
    return str(db)

try:
    database.connection

    @bot.message_handler(commands=['start'])
    def start_message(message):
        db = (f"id{message.from_user.id}")
        database.create_table(db)
        commands.start(message)


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        chatID = message.chat.id
        match message.text:
            case "Добавить задачу":
                database.add_tasks(message)

            case "Посмотреть задачи":
                database.show_tasks(bot, message)

            case "Очистить список":
                database.clear_db(bot, message)

            case "Главная":
                bot.send_message(chatID, messages.hello(bot, message))
   

except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
