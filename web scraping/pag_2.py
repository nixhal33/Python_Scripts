import requests
from bs4 import BeautifulSoup
import os

root_website = 'https://subslikescript.com'
secondary_website = f'{root_website}/movies_letter-S'
result = requests.get(secondary_website)
content = result.text
soup = BeautifulSoup(content,'lxml')
# print(soup.prettify())

# for pagination
pagination = soup.find('ul',class_='pagination')
pages = pagination.find_all('li', class_='page-item')

# simple entire div class for the movies title and their link div
main_box = soup.find('article', class_='main-article')


