''' JavaScript Object Notation '''

import json
from modules import utils
from urllib.request import urlopen
from urllib.error import URLError

# APIURL = 'https://jsonplaceholder.typicode.com/photos'
JSON_NAME='users'
APIURL = 'https://jsonplaceholder.typicode.com/' + JSON_NAME
#######################################################################################################
utils.banner(
    'download JSON from online public API:',
    APIURL
)
#######################################################################################################
try:
    with urlopen(APIURL) as response:
        print(f'response status: {response.status}')
        source = response.read()
except URLError as ue:
    print(ue)
    print('falling back to: ', utils.getdatafilepath(JSON_NAME))
    try:
        with open(utils.getdatafilepath(JSON_NAME)) as photos:
            source = photos.read()
    except FileNotFoundError as fnfe:
        print(fnfe)
        print('quitting...')
        exit(1)

maxchars = 400
print(f'dumping first {maxchars} chars:')
utils.dashline()
print(source[0:400])
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
print('type of data    | ', type(data))
print('length of data  |', len(data))
print('data[0]         | ', data[0])
print('type of data[0] | ', type(data[0]))
#######################################################################################################
utils.banner(
    'list some records of JSON obj',
)
#######################################################################################################
for photo in range(0, 10):
    print(data[photo])
#######################################################################################################
utils.banner(
    'pretty print one record',
)
#######################################################################################################
print(json.dumps(data[0], indent=2))
