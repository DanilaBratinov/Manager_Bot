import web
import news

from user import get_name, get_id

def hello(message):
    hello_message = f"""
☘️Привет, {get_name(message)}☘️

⌚️Сегодняшняя дата: {web.get_date.today('Europe/Moscow').format('DD.MM.YYYY')}
{web.get_weather('Москва')}

Актуальные новости:\n{news.get_news()}
"""


    
    return hello_message