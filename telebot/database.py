import pymysql

def create_table(connection):
    # db = (f"id{message.from_user.id}")
    db = "id1123"
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE TABLE {str(db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")
        connection.commit()