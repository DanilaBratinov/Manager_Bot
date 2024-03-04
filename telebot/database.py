import web
import commands
import pymysql
from telebot import types
from config import host, user, password, db_name

bot = commands.bot

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
def create_table():
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE {str(get_db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")

        connection.commit()

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
        # return ("\n".join(task))
    
# Clear all task
def clear_db(db, bot, message):

    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {str(get_db)};")
        connection.commit()

    bot.send_message(message.chat.id, "Список очищен!")