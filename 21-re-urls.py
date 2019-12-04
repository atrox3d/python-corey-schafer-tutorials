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
#
# loop over matches
#
for match in matches:
    #
    #   loop over groups inside every match
    #
    groups = []
    for group in match.groups():
        #
        # format every group
        #
        group = "" if group is None else group
        groups.append(f'{group:<10}')
    #
    #   add the entire match : group 0
    #
    line = f'{match.group(0):<25}, '
    #
    #   join formatted groups
    #
    line += ", ".join(groups)
    print(line)

