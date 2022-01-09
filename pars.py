'''
Парсинг сайта Яндкерка по новостям
'''

import requests
from bs4 import BeautifulSoup


base = 'https://www.yandex.ru'
html = requests.get(base).content
soup = BeautifulSoup(html, 'lxml')
div = soup.find('div', id="news_panel_news")
ahref = div.find_all('a', class_='home-link2 news__item list__item-content list__item-content_with-icon home-link2_color_inherit home-link2_hover_red')
span = div.find_all('span', class_='news__item-content')


if __name__ == '__main__':
    j = 1
    spantext = []
    for i in span:

        print(f'{j}. ' + i.getText())
        j += 1