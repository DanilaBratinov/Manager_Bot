import web
import news

from user import get_name

def hello(message):
    hello_message = f"""
        ☘️Привет, {get_name(message)}☘️

        ⌚️Сегодняшняя дата: {web.get_date('Сегодня')}
        {web.get_weather('Москва')}

        Актуальные новости:\n{news.get_news()}
        """

    return hello_message
