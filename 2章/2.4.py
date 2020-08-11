from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src': re.compile('..\/img\/gifts\/img.*.jpg')})
trs = bs.find_all('tr', {'class' : re.compile('^gift$')})

for image in images:
    print(image['src'])
    print(image)

for tr in trs:
    print(tr['id'])
    print(tr['class'])