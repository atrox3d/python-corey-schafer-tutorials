from modules import utils
import os.path
from bs4 import BeautifulSoup
import requests


def print_partial_html(text, maxlines=10):
    """
    print partial html to get cleaner output
    :param text:
    :param maxlines:
    :return:
    """

    utils.dashline()

    if maxlines is not None:                                    # if we have maxline arguments process it
        text = text.split('\n')                                 # make sure that we have a list of lines (\n)
        if len(text) > maxlines:                                # if the number of lines is greater than maxlines
            for _ in range(0, maxlines):                        # print only until maxlines
                print(text[_])
            print('...')                                        # make it clear that the text is longer
            print('...')
            print('...')
        else:
            print(text)                                         # the text is less longer than maxline, print all
    else:
        print(text)                                             # no maxlines, print all

    utils.dashline()


########################################################################################################################
utils.banner(
    'https://www.youtube.com/watch?v=ng2o98k983k',
    'web scraping with beautiful soup',
    'http://coreyms.com'
)

request = requests.get('http://coreyms.com')                        # execute request
print(f'request to http://coreyms.com: {request}')                  # print request http status

source = request.text                                               # extract request text (html)
print(f'request html source: ')
print_partial_html(source)

########################################################################################################################
utils.banner('parse source with BeautifulSoup (prettify)')

soup = BeautifulSoup(source, 'lxml')                                # parse html with BeautifulSoup via lxml
print_partial_html(soup.prettify())
########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '1) find article'
)

article = soup.find('article')                                      # find tag article inside soup obj
print_partial_html(article.prettify())
########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '2) get headline'
)

headline = article.h2.a.text                                        # navigate to link text
headline2 = article.a.text                                          # same, different syntax
print(f'article.h2.a.text: {headline!r}')
print(f'article.a.text   : {headline2!r}')
########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '3) get summary'
)

summary = article.find('div', class_='entry-content')               # extract div from article obj
print(f'{summary.p.text!r}')
########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '4) get video link'
)

# video_source = article.find('iframe', class_='youtube-player')    # there is no more class in html
video = article.find('iframe')                                      # get iframe inside article
print(video)
utils.dashline()

print(video.__dict__)                                               # display video obj dictionary
utils.dashline()

utils.banner('video tag attrs:')
for k, v in video.attrs.items():                                    # display tag attributes
    print(f'{k:<20} = {v}')
utils.dashline()

video_src = video['src']                                            # display video src
print('video.src: ', video_src)

########################################################################################################################
utils.banner(
    'parse source with BeautifulSoup',
    '5) get only video ID'
)

video_url = video_src.split('?')[0]
print('video url w/o query parameters: ', video_url)

videourl_parts = video_url.split('/')
video_id = videourl_parts[-1]
print('video ID: ', video_id)
