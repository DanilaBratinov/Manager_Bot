import requests

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