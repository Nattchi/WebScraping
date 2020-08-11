from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
print("-----bs4-----")
print(bs.find_all('', text='Or maybe he\'s only resting?'))
print("-----lambda-----")
print(bs.find_all(lambda tag : tag.get_text() == 'Or maybe he\'s only resting?'))
double_attrs = bs.find_all(lambda tag: len(tag.attrs) == 2)

for double_attr in double_attrs:
    print(double_attr)