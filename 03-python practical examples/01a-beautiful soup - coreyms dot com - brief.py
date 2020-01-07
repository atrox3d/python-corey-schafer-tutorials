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

request = requests.get('http://coreyms.com')                        # execute request
print(f'request to http://coreyms.com: {request}')                  # print request http status

source = request.text                                               # extract request text (html)
# print(f'request html source: ')
# print_partial_html(source)

########################################################################################################################
utils.banner('parse source with BeautifulSoup (prettify)')

soup = BeautifulSoup(source, 'lxml')                                # parse html with BeautifulSoup via lxml
# print_partial_html(soup.prettify())
########################################################################################################################
for article in soup.find_all('article'):                                      # find tag article inside soup obj
    # utils.banner(
    #     'parse source with BeautifulSoup',
    #     '1) find article'
    # )
    #
    # print_partial_html(article.prettify())
    ########################################################################################################################
    # utils.banner(
    #     'parse source with BeautifulSoup',
    #     '2) get headline'
    # )

    headline = article.h2.a.text                                        # navigate to link text
    headline2 = article.a.text                                          # same, different syntax
    # print(f'article.h2.a.text: {headline!r}')
    # print(f'article.a.text   : {headline2!r}')
    print(f'{headline2!r}')
    ########################################################################################################################
    # utils.banner(
    #     'parse source with BeautifulSoup',
    #     '3) get summary'
    # )

    summary = article.find('div', class_='entry-content')               # extract div from article obj
    print(f'{summary.p.text!r}')
    ########################################################################################################################
    # utils.banner(
    #     'parse source with BeautifulSoup',
    #     '4) get video link'
    # )

    # video_source = article.find('iframe', class_='youtube-player')    # there is no more class in html
    video = article.find('iframe')                                      # get iframe inside article
    # print(video)
    if video is not None:
        # utils.dashline()
        #
        # print(video.__dict__)                                               # display video obj dictionary
        # utils.dashline()
        #
        # utils.banner('video tag attrs:')
        # for k, v in video.attrs.items():                                    # display tag attributes
        #     print(f'{k:<20} = {v}')
        # utils.dashline()
        #
        video_src = video['src']                                            # display video src
        # print('video.src: ', video_src)

        ########################################################################################################################
        # utils.banner(
        #     'parse source with BeautifulSoup',
        #     '5) get only video ID'
        # )
        #
        video_url = video_src.split('?')[0]
        # print('video url w/o query parameters: ', video_url)

        videourl_parts = video_url.split('/')
        video_id = videourl_parts[-1]
        # print('video ID: ', video_id)
        ########################################################################################################################
        # utils.banner(
        #     'parse source with BeautifulSoup',
        #     '6) create youtube link'
        # )

        yt_link = f'https://youtube.com/watch?v={video_id}'
        print('video link: ', yt_link)
    print()
