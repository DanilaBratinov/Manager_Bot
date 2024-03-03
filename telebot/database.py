def create_table(connection):
    # db = (f"id{message.from_user.id}")
    db = "id1123"
    with connection.cursor() as cursor:
        query = f"SHOW TABLES LIKE '{db}'"
        cursor.execute(query)
        result = cursor.fetchone()

        # cursor.execute(f"CREATE TABLE {str(db)} (id int AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), time VARCHAR(255), date VARCHAR(255), lon VARCHAR(255), lat VARCHAR(255))")
        if result:
            print(f"Таблица существует")
        else:
            print(f"Таблица не существует")

        # connection.commit()