import web
import pymysql

from config import host, user, password, db_name

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

def get_db(message):
    db = (f"id{message.from_user.id}")

    return db

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
        cursor.execute(f"CREATE TABLE {str(db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")

        connection.commit()



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
        select_all_rows = f"SELECT time, name, date FROM {str(db)} ORDER BY STR_TO_DATE(time, '%H:%i');"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        tasks = ['']

        for row in rows:
            tasks.append("🌵{time} – {name}".format(**row))
        
        connection.commit()

        return ("\n".join(tasks))