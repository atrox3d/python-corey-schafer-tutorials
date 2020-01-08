''' JavaScript Object Notation '''

import json
from modules import utils
from urllib.request import urlopen
from urllib.error import URLError

#######################################################################################################
utils.banner(
    'download JSON from online public API:',
    'https://jsonplaceholder.typicode.com/photos'
)
#######################################################################################################
APIURL = 'https://jsonplaceholder.typicode.com/photos'
try:
    with urlopen(APIURL) as response:
        print(f'response status: {response.status}')
        source = response.read()
except URLError as ue:
    print(ue)
    print('falling back to: ', utils.getdatafilepath('photos.json'))
    try:
        with open(utils.getdatafilepath('photos.json')) as photos:
            source = photos.read()
    except FileNotFoundError as fnfe:
        print(fnfe)
        print('quitting...')
        exit(1)

maxchars = 400
print(f'dumping first {maxchars} chars:')
utils.dashline()
print(source[0:400])
utils.dashline()
#######################################################################################################
utils.banner(
    'converto to JSON',
)
#######################################################################################################
data = json.loads(source)
data_pretty = json.dumps(data, indent=2)
data_prettylist = data_pretty.split('\n')
for line in range(0, 20):
    print(data_prettylist[line])
print('------X----------X---------X-------')
