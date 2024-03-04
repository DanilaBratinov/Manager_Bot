import commands
import database
import messages
import web
bot = commands.bot

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
        chatID = message.chat.id
        match message.text:
            case "Добавить задачу":
                add_tasks(message)
            case "Посмотреть задачи":
                # bot.send_message(chatID, database.show_tasks(db))
                database.show_tasks(bot, message)

            case "Очистить список":
                database.clear_db(get_db, bot, message)
                # bot.send_message(chatID, "Список очищен")

            case "Главная":
                bot.send_message(chatID, messages.hello(message))
    
    task = ["", "", ""] 

    def add_tasks(message):
        bot.send_message(message.chat.id, 'Введите название задачи:')
        bot.register_next_step_handler(message, add_task_name)
    #Название задачи
    def add_task_name(message):
        task[0] = message.text
        bot.send_message(message.chat.id, "Введите время:")
        bot.register_next_step_handler(message, add_task_time)

    #Время
    def add_task_time(message):
        task[1] = (message.text)

        markup = commands.types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = commands.types.KeyboardButton('Сегодня')
        item2 = commands.types.KeyboardButton('Завтра')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Выберите дату:", reply_markup = markup)
        bot.register_next_step_handler(message, add_task_date(message))
                        
    #Дата
    def add_task_date(message):
        task[2] = web.get_date('Сегодня').format('DD.MM.YYYY')

        with database.connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO id{message.chat.id}' (time, name, date) VALUES ('{task[1]}', '{task[0]}', '{task[2]}');")
            database.connection.commit()

            markup = commands.types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = commands.types.KeyboardButton('Добавить задачу')
            item2 = commands.types.KeyboardButton('Посмотреть задачи')
            item3 = commands.types.KeyboardButton('Очистить список')
            item4 = commands.types.KeyboardButton('Главная')

            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, f"Добавлена задача: *{task[0]}*", parse_mode="Markdown", reply_markup = markup)

except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
