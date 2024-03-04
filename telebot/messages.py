import web
import database
from commands import bot
import news
from user import get_name

def hello(message):
    hello_message = f"""
☘️Привет, {get_name(message)}☘️
***********************************
{database.show_tasks(bot, message)}
***********************************
⌚️Сегодняшняя дата: {web.get_date('Сегодня').format('DD.MM.YYYY')}
{web.get_weather('Москва')}

Актуальные новости:\n{news.get_news()}
"""

    return hello_message
