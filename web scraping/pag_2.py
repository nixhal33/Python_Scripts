import requests
from bs4 import BeautifulSoup
import os

root_website = 'https://subslikescript.com'
secondary_website = f'{root_website}/movies'
result = requests.get(secondary_website)
content = result.text
soup = BeautifulSoup(content,'lxml')
