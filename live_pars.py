import requests
from bs4 import BeautifulSoup
import json
import time
import random as rand


book_links_list = {}
for page in range(0, 87, 1):
    url = f'https://knigogid.ru/books/page-{page}'
    q = requests.get(url)
    result = q.content  # собираем ссылки на страницы с книгами

    soup = BeautifulSoup(result, "html.parser")

    book_hrefs = soup.find_all(class_='b-item-name')

    for href in book_hrefs:
        book_links = 'https://knigogid.ru'+href.get('href')
        book_links_list[book_links] = href

with open('book_links_list', 'a') as file:
    for line in book_links_list:
        file.write(f'{line}\n')  # записываем ссылки на книги в файл

data_dict = []
count = 0
with open('book_links_list') as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    q = requests.get(line)
    result = q.content

    # while True:
    #     try:
    #         q = requests.get('https://www.kinogid.ru'+line)
    #         result = q.content
    #         break
    #     except:
    #         time.sleep(5)

    soup = BeautifulSoup(result,  "html.parser")

    title = soup.find(class_='b-book-name').text
    series = soup.find(class_='b-book-series').text
    rate = soup.find(class_="b-item-rate").text
    views = soup.find('li').find('span').text
    author = soup.find(class_='b-book-user__name').text

    data = {
        'title': title,
        'author': author,
        'rate': rate,
        'views': views,
        'series': series
    }
    print(f'#{count}:{lines} is done!')
    data_dict.append(data)

    with open('data.json', 'w') as file:
        json.dump(data_dict, file, indent=4, ensure_ascii=False)# сохраняем данные в json-файл для дальнейшей работы с ними
