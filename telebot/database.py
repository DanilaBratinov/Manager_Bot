import web
import pymysql

from config import host, user, password, db_name

# Connect to MySQL-Server
def connection():
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    return connection

# Get DB-ID user 
def get_db(message):
    db = (f"id{message.from_user.id}")

    return db

# Create table on user
def create_table(db):
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE {str(get_db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")

        connection.commit()

# Add task
def add_task_one(bot, message):
        bot.send_message(message.chat.id, 'Введите название задачи:')
        # bot.register_next_step_handler(message, add_task_two)

task = ["", "", ""] 

# Show today tasks
def show_tasks(db):
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    with connection.cursor() as cursor:
        select_all_rows = f"SELECT time, name, date FROM {str(get_db)} WHERE date = '{web.get_date('Сегодня')}' ORDER BY STR_TO_DATE(time, '%H:%i');"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        tasks = ['']

        for row in rows:
            tasks.append("🌵{time} – {name}".format(**row))
        
        connection.commit()

        return ("\n".join(tasks))
    
# Clear all task
def clear_db(db):
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )

    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {str(get_db)};")
        connection.commit()