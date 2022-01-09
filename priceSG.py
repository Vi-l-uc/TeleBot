"""
Парсинг цен сайта Станкоград на точильно-шлифовальные станки
"""


import requests
from bs4 import BeautifulSoup


def price():
    adress_sg = ["https://pkfstankograd.ru/catalog/tochilno-shlifovalnye-stanki/",
                 "https://pkfstankograd.ru/catalog/tochilno-shlifovalnye-stanki/?PAGEN_2=2",
                 "https://pkfstankograd.ru/catalog/tochilno-shlifovalnye-stanki/?PAGEN_2=3"]

    pri = []
    it = []

    for i in adress_sg:

        base = i
        html = requests.get(base).content
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_='catalog-section-items')
        a = div.find_all('a', class_='catalog-section-item-name-wrapper intec-cl-text-hover')
        span = div.find_all(attrs={"data-role": "item.price.discount"})

        for i in a:
            it.append((i.getText()))

        for i in span:
            pri.append(' '.join(i.getText().split()))

    pricesg = {it[i]: pri[i] for i in range(len(it))}

    return pricesg


def main():
    pricesg = price()

    for i in pricesg:
        print(i + ' - ' + pricesg[i])


if __name__ == '__main__':
    main()
