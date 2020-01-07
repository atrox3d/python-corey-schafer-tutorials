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

request = requests.get('http://coreyms.com')                            # execute request
print(f'request to http://coreyms.com: {request}')                      # print request http status

source = request.text                                                   # extract request text (html)
########################################################################################################################
utils.banner('parse source with BeautifulSoup (prettify)')

soup = BeautifulSoup(source, 'lxml')                                    # parse html with BeautifulSoup via lxml
########################################################################################################################
for article in soup.find_all('article'):                                # find tag article inside soup obj
    headline = article.h2.a.text                                        # navigate to link text
    headline2 = article.a.text                                          # same, different syntax
    print(f'{headline2!r}')

    summary = article.find('div', class_='entry-content')               # extract div from article obj
    print(f'{summary.p.text!r}')

    video = article.find('iframe')                                      # get iframe inside article

    if video is not None:
        video_src = video['src']                                        # display video src
        video_url = video_src.split('?')[0]                             # get left part of url before ?

        videourl_parts = video_url.split('/')                           # get url tokens split by /
        video_id = videourl_parts[-1]                                   # finally, get id

        yt_link = f'https://youtube.com/watch?v={video_id}'             # create link
        print(yt_link)

    print()
