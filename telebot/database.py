def create_table(connection, message):
    db = (f"id{message.from_user.id}")

    def check_table():
        with connection.cursor() as cursor:
            query = f"SHOW TABLES LIKE '{db}'"
            cursor.execute(query)
            result = cursor.fetchone()
            return result

    with connection.cursor() as cursor:
        if check_table(connection):
            print("существует")
        else:
            cursor.execute(f"CREATE TABLE {str(db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")

        connection.commit()