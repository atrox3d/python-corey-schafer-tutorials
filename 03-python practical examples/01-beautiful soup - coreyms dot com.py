from modules import utils
import os.path
from bs4 import BeautifulSoup
import requests


def print_partial_html(text, maxlines=None):
    utils.dashline()

    if maxlines is not None:
        text = text.split('\n')
        for _ in range(0, maxlines):
            print(text[_])
    else:
        print(text)

    print('...')
    utils.dashline()


########################################################################################################################
utils.banner(
    'https://www.youtube.com/watch?v=ng2o98k983k',
    'web scraping with beautiful soup',
    'http://coreyms.com'
)

request = requests.get('http://coreyms.com')  # execute request
print(f'request to http://coreyms.com: {request}')  # print request http status

source = request.text  # extract request text (html)
print(f'request html source: ')
print_partial_html(source, 10)
exit()

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

########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '4) get video link'
)

# video_source = article.find('iframe', class_='youtube-player')    # there is no more class in html
video = article.find('iframe')
print(video)
utils.dashline()

print(video.__dict__)
utils.dashline()

utils.banner('video tag attrs:')
for k, v in video.attrs.items():
    print(f'{k:<20} = {v}')
utils.dashline()

video_src = video['src']
print(video_src)
