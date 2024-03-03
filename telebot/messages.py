import web
import news
import database
from user import get_name

def hello(message):
    hello_message = f"""
☘️Привет, {get_name(message)}☘️
******************************

⌚️Сегодняшняя дата: {web.get_date('Сегодня').format('DD.MM.YYYY')}
{web.get_weather('Москва')}

Актуальные новости:\n{news.get_news()}
"""

    return hello_message

# {database.show_tasks(database.connection, database.get_db)}