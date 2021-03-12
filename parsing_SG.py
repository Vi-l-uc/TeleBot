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
        div = soup.find('div', class_='group-content')
        a = div.find_all('span', class_='btn btn-primary btn-sm')
        span = div.find_all('span', class_='price_val')

        for i in a:
            it.append((i.get('data-product')))

        for i in span:
            pri.append(i.getText())

    pricesg = {it[i]: pri[i] for i in range(len(it))}

    return pricesg


def main():
    pricesg = price()

    for i in pricesg:
        print(i + ' - ' + pricesg[i])


if __name__ == '__main__':
    main()
