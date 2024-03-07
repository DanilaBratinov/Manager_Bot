import requests
import pendulum

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

    weather = f'☃️Температура в {locate}: {temperature}°C\n☃️Температура дома: {temperature2}°C'
    return weather

def get_usd_to_rub_exchange_rate():
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = response.json()
    
    usd_to_rub_exchange_rate = data['Valute']['USD']['Value']
    return usd_to_rub_exchange_rate

def get_date(when):
    match when:
        case 'Сегодня':
            date = pendulum.today('Europe/Moscow').format('DD.MM')
        case 'Завтра':
            date = pendulum.tomorrow('Europe/Moscow').format('DD.MM')
    return date.format('DD.MM.YYYY')