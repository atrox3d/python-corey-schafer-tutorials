from modules import utils
import os.path
from bs4 import BeautifulSoup
import requests

########################################################################################################################
utils.banner(
    'https://www.youtube.com/watch?v=ng2o98k983k',
    'web scraping with beautiful soup',
    'http://coreyms.com'
)

request = requests.get('http://coreyms.com')
print(f'request to http://coreyms.com: {request}')

source = request.text
print(f'request html source: ')

utils.dashline()
print(f'{source}')
utils.dashline()

########################################################################################################################
utils.banner('parse source with BeautifulSoup')

soup = BeautifulSoup(source, 'lxml')
print(soup.prettify())

########################################################################################################################
utils.banner(
                'parse source with BeautifulSoup',
                '1) find article'
)

article = soup.find('article')
print(article.prettify())

########################################################################################################################
utils.banner(
                'parse source with BeautifulSoup',
                '2) get headline'
)

headline = article.h2.a.text
headline2 = article.a.text
print(f'article.h2.a.text: {headline!r}')
print(f'article.a.text   : {headline2!r}')


########################################################################################################################
utils.banner(
                'parse source with BeautifulSoup',
                '3) get summary'
)

summary = article.find('div', class_='entry-content')
# print(f'{summary.text!r}')
print(f'{summary.p.text!r}')

