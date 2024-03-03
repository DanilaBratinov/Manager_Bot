import pendulum
import requests

import telebot
import main

token = '6556635188:AAHgGkjUlc_lzhdQt_QgvEYMtClLyLdOBQE'
bot = telebot.TeleBot(token)

# Приветственный текст
def hello_text(message):
    db = (f"id{message.from_user.id}")

    text = f"☘️Привет, {message.from_user.first_name}☘️\n***********************************{main.show_tasks(db)}\n***********************************\n⌚️Сегодняшняя дата: {pendulum.today('Europe/Moscow').format('DD.MM.YYYY')}\n{function.get_weather('Москва')}\n💸Курс USD: {format(function.get_usd_to_rub_exchange_rate())}₽"

    return text

# Получение актуальной даты
def get_date(when):
    match when:
        case 'Сегодня':
            date = pendulum.today('Europe/Moscow').format('DD.MM')
        case 'Завтра':
            date = pendulum.tomorrow('Europe/Moscow').format('DD.MM')
    return date

# Получение курса валют
def get_usd_to_rub_exchange_rate():
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    return data['Valute']['USD']['Value']

# Получение данных о погоде
def get_weather(locate):
    api_key = '28ede8c4626bcba101f47c928f53f1b9'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={locate}&appid={api_key}&units=metric'
    url2 = f'http://api.openweathermap.org/data/2.5/weather?lat=56.051012&lon=37.992539&appid={api_key}&units=metric'

    response = requests.get(url)
    response2 = requests.get(url2)

    data = response.json()
    data2 = response2.json()

    temperature = data['main']['temp']
    temperature2 = data2['main']['temp']

    weather = f'☃️Температура в {locate}: {temperature}°C\n☃️Температура дома: {temperature2}°C\n'
    return weather