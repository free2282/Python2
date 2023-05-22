import re
import ssl
from urllib.request import Request, urlopen
from statistics import mean 

ssl._create_default_https_context = ssl._create_unverified_context

def get_product_names(html):
    regex = re.compile(r'<a class="b-card2-v2__name"[^>]*>(.*)<', re.IGNORECASE | re.MULTILINE)
    values = re.findall(regex, html)
    return list(map(lambda x: x.strip(), values))

def get_product_prices(html):
    regex = re.compile(r'<span class="b-card2-v2__price-val"[^>]*>(.*)<', re.IGNORECASE | re.MULTILINE)
    sub = re.compile('[,. ]')
    values = re.findall(regex, html)
    return list(map(lambda price: int(sub.sub('', price)), values))

url = 'https://quke.ru/shop/smartfony/apple?page-size=72'

request = Request(url)
with urlopen(request) as response:
    body = response.read().decode('utf-8')

product_names = get_product_names(body)
product_prices = get_product_prices(body)
products = list(zip(product_names, product_prices))

mostExpensive = max(products, key=lambda product: product[1])
cheapest = min(products, key=lambda product: product[1])
avgPrice = round(mean(map(lambda product: product[1], products)), 2)

print(f'Самый дорогой товар: {mostExpensive[0]} {mostExpensive[1]}₽')
print(f'Самый дешёвый товар: {cheapest[0]} {cheapest[1]}₽')
print(f'Средняя цена: {avgPrice}₽')

with open('catalog.txt', 'w', encoding="utf-8") as catalog:
    for name, price in products:
        catalog.write(f'{name} | {price}\n')