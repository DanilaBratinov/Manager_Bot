import web
from  commands import bot
import pymysql
from telebot import types
from config import host, user, password, db_name

# Connect to MySQL-Server
connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
)
# Get DB-ID user 
def get_db(message):
    db = (f"id{message.from_user.id}")

    return db

# Create table on user
def create_table(message):
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE id{message.chat.id} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")

        connection.commit()


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

    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Сегодня')
    item2 = types.KeyboardButton('Завтра')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, "Выберите дату:", reply_markup = markup)
    bot.register_next_step_handler(message, add_task_date)
                        
    #Дата
def add_task_date(message):
    task[2] = web.get_date(message.text)

    with connection.cursor() as cursor:
        cursor.execute(f"INSERT INTO id{message.chat.id} (time, name, date) VALUES ('{task[1]}', '{task[0]}', '{task[2]}');")
        connection.commit()

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Добавить задачу')
        item2 = types.KeyboardButton('Посмотреть задачи')
        item3 = types.KeyboardButton('Очистить список')
        item4 = types.KeyboardButton('Главная')

        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f"Добавлена задача: *{task[0]}*", parse_mode="Markdown", reply_markup = markup)

# Show today tasks
def show_tasks(bot, message):
    with connection.cursor() as cursor:
        select_all_rows = f"SELECT time, name, date FROM id{message.chat.id} WHERE date = '{web.get_date('Сегодня')}' ORDER BY STR_TO_DATE(time, '%H:%i');"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        task = ['']

        for row in rows:
            task.append("🌵{time} – {name}".format(**row))
        
        connection.commit()

        tasks = ("\n".join(task))
        bot.send_message(message.chat.id, tasks)
    
# Clear all task
def clear_db(bot, message):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM id{message.chat.id};")
        connection.commit()

    bot.send_message(message.chat.id, "Список очищен!")