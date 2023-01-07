import requests
from bs4 import BeautifulSoup

import time
import random as rand

review_dict = {'name': [], 'date': [], 'rating': [], 'review': []}
# думаю, тут можно побольше всего добавить, если код
# норм отработает

for page in range(0, 23):  # Кол-во страниц можно поменять на большее, если норамльно парситься будет
    url = f'https://www.metacritic.com/game/user-reviews?page={page}'  # не уверен, что ссылка именно такая должна быть
    user_agent = {'User-agent': 'Mozilla/5.0'}  # юзер-агент тоже надо будет подставить
    response = requests.get(url, headers=user_agent)
    time.sleep(rand.randint(3, 30))  # можно затраить без промежутков, либо наоборот увеличить интервал
    soup = BeautifulSoup(response.text, 'html.parser')
    for review in soup.find_all('div',
                                class_=''):  # здесь и далее в классах нужно указывать классы, где лежат нужные нам
        # данные
        if review.find('div', class_='name') is None:
            break
            
        review_dict['name'].append(review.find('div', class_='').find('a').text)
        # хз, понадобяться нам два фаинда или нет
        review_dict['date'].append(review.find('div', class_='').text)
        # текст можно дропнуть, если там тупо цифры будут
        review_dict['rating'].append(review.find('div', class_='').find_all('div')[0].text)
        if review.find('span', class_=''):
            review_dict['review'].append(review.find('span', class_='').text)
        # здесь может быть нихуя не span
        else:
            review_dict['review'].append(
                review.find('div', class_='').find('span').text)  # хз, понадобяться нам два фаинда или нет
