import news
import telebot
from telebot import types
import web

from user import get_name
from user import get_id

import pymysql
from config import host, user, password, db_name

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

get_usd = web.get_usd_to_rub_exchange_rate()

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
        chatID = message.chat.id

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Добавить задачу')
        item2 = types.KeyboardButton('Посмотреть задачи')
        item3 = types.KeyboardButton('Очистить список')
        item4 = types.KeyboardButton('Главная')

        markup.add(item1, item2, item3, item4)

        db = (f"id{message.from_user.id}")

        with connection.cursor() as cursor:
            cursor.execute(f"CREATE TABLE {str(db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")
            connection.commit()
        bot.send_message(chatID, f"☘️Привет, {get_name(message)}☘️\n\n***********************************{show_tasks(db)}\n***********************************\n\n⌚️Сегодняшняя дата: {web.get_date.today('Europe/Moscow').format('DD.MM.YYYY')}\n\n{web.get_weather('Москва')}\n💸Курс USD: {format(get_usd)}₽\n\nАктуальные новости:\n{news.get_news()}", reply_markup = markup)


    @bot.message_handler(content_types=['text'])
    def send_message(message):
        chatID = message.chat.id
        db = (f"id{message.from_user.id}")

        match message.text:
            case "Добавить задачу":
                add_task_one(message)

            case "Посмотреть задачи":
                bot.send_message(chatID, show_tasks(db))
            
            case "Очистить список":
                with connection.cursor() as cursor:
                    cursor.execute(f"DELETE FROM {str(db)};")
                    connection.commit()
                    bot.send_message(chatID, "Список очищен!")

            case "Главная":
                bot.send_message(chatID, f"☘️Привет, {get_name(message)}☘️\n\n***********************************{show_tasks(db)}\n***********************************\n\n⌚️Сегодняшняя дата: {web.get_date.today('Europe/Moscow').format('DD.MM.YYYY')}\n\n{web.get_weather('Москва')}\n💸Курс USD: {format(get_usd)}₽\n\nАктуальные новости:\n{news.get_news()}")


    def add_task_one(message):
        bot.send_message(message.chat.id, 'Введите название задачи:')
        bot.register_next_step_handler(message, add_task_two)

    task = ["", "", ""]
    
    #Название задачи
    def add_task_two(message):
        task[0] = message.text
        bot.send_message(message.chat.id, "Введите время:")
        bot.register_next_step_handler(message, add_task_three)
    #Время
    def add_task_three(message):
        task[1] = (message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Сегодня')
        item2 = types.KeyboardButton('Завтра')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, "Выберите дату:", reply_markup = markup)
        bot.register_next_step_handler(message, add_task_four)
    #Дата
    def add_task_four(message):
        task[2] = web.get_date(message.text)

        db = (f"id{get_id(message)}")
        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO {str(db)} (time, name, date) VALUES ('{task[1]}', '{task[0]}', '{task[2]}');")
            connection.commit()

        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Добавить задачу')
        item2 = types.KeyboardButton('Посмотреть задачи')
        item3 = types.KeyboardButton('Очистить список')
        item4 = types.KeyboardButton('Главная')

        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f"Добавлена задача: *{task[0]}*", parse_mode="Markdown", reply_markup = markup) 
    
    def show_tasks(db):
        with connection.cursor() as cursor:
            select_all_rows = f"SELECT time, name, date FROM {str(db)} WHERE date = '{web.get_date('Сегодня')}' ORDER BY STR_TO_DATE(time, '%H:%i');"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
            tasks = ['']

            for row in rows:
                tasks.append("🌵{time} – {name}".format(**row))
            connection.commit()

            return ("\n".join(tasks))

except Exception as ex:
    print("Ошибка подключения к базе данных...")
    print(ex)

bot.infinity_polling()
