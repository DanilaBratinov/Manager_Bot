import requests
from bs4 import BeautifulSoup
def get_news():
    url = 'https://www.rbc.ru/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    news = soup.find('span', class_='main__big__title').text.strip()
    news2 = soup.find('span', class_='main__feed__title').text.strip()

    return (f'📰{news}\n📰{news2}')
    