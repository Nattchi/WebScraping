from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

print("-----Simple-----")
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print("-----Regex-----")
for link in bs.find('div', {'id': 'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')
):
    if 'href' in link.attrs:
        print(link.attrs['href'])

print("-----Complete-----")
random.seed(datetime.datetime.now())
en_targetUrl = 'http://en.wikipedia.org'
ja_targetUrl = 'http://ja.wikipedia.org'

def getLinks(articleUrl):
    html = urlopen((en_targetUrl + '{}').format(articleUrl))
    bs = BeautifulSoup(html, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# links = getLinks('/wiki/Kevin_Bacon')
links = getLinks('/wiki/BanG_Dream!')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)
