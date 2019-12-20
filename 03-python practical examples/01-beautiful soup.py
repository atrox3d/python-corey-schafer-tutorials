from modules import utils
import os.path
from bs4 import BeautifulSoup
import requests

########################################################################################################################
utils.banner(
    'https://www.youtube.com/watch?v=ng2o98k983k',
    'web scraping with beautiful soup',
    f'PROJECT_PATH    : {utils.PROJECT_PATH}',
    f'PROJECTDATA_PATH: {utils.PROJECTDATA_PATH}',
)

html_path = os.path.join(utils.PROJECTDATA_PATH, 'simple.html')

print('HTML FILE DUMP:')
utils.hashline(char='-')
with open(html_path) as html_file:              #
    print(html_file.read())

with open(html_path) as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

########################################################################################################################
utils.banner('HTML SOUP DUMP (prettified):')
print(soup.prettify())

########################################################################################################################
utils.banner('matching tags')
match_title = soup.title
print(f'.title:')
utils.hashline(char='-')
print(f'{match_title}')
utils.hashline(char='-')
print(f'.title.text:')
utils.hashline(char='-')
print(f'{match_title.text}')
print()
match_div = soup.div
utils.hashline(char='-')
print(f'.div:')
utils.hashline(char='-')
print(f'{match_div}')

########################################################################################################################
utils.banner('find tags')

find_div = soup.find('div')
print(f'find div:')
utils.hashline(char='-')
print(f'{find_div}')

find_divfooter = soup.find('div', class_='footer')
utils.hashline(char='-')
print(f'find div/footer:')
utils.hashline(char='-')
print(f'{find_divfooter}')

########################################################################################################################
utils.banner('find article and subtags')

article = soup.find('div', class_='article')
print('article div:')
utils.hashline(char='-')
print(article)

headline = article.h2.a.text
utils.hashline(char='-')
print('article anchor text:')
utils.hashline(char='-')
print(headline)

utils.hashline(char='-')
print('article paragraph:')
utils.hashline(char='-')
summary = article.p.text
print(summary)

