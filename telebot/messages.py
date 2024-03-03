import web
import news

from user import get_name, get_id

hello_message = f"☘️Привет, {get_name(message)}☘️\n\n***********************************{show_tasks(db)}\n***********************************\n\n⌚️Сегодняшняя дата: {web.get_date.today('Europe/Moscow').format('DD.MM.YYYY')}\n\n{web.get_weather('Москва')}\n💸Курс USD: {format(web.get_usd)}₽\n\nАктуальные новости:\n{news.get_news()}"