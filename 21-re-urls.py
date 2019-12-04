#
#   https://www.youtube.com/watch?v=K8L6KVGG-7o
#
#################################################################################
import utils
import re
from collections import namedtuple
import os


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

#
#   3 groups:
#       - optional www
#       - domain name
#       - top level domain
#
topleveldomain = r'https?://(www\.)?(\w+)(\.\w+)'
pattern = re.compile(topleveldomain)

matches = pattern.finditer(urls)

for match in matches:
    groups = []
    for group in match.groups():
        group = "" if group is None else group
        groups.append(f'{group:<10}')

    line = f'{match.group(0):<25}, '
    line += ", ".join(groups)
    print(line)

