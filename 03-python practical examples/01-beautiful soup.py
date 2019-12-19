from modules import utils
import os.path
from bs4 import BeautifulSoup
import requests

utils.banner(
    'https://www.youtube.com/watch?v=ng2o98k983k',
    'web scraping with beautiful soup',
    f'PROJECT_PATH    : {utils.PROJECT_PATH}',
    f'PROJECTDATA_PATH: {utils.PROJECTDATA_PATH}',
)

html_path = os.path.join(utils.PROJECTDATA_PATH, 'simple.html')
# with open(html_path, 'r'):    # read is the default
with open(html_path) as html_file:
    print('HTML CONTENT:')
    utils.hashline(char='-')
    print(html_file.read())
    utils.hashline(char='-')
