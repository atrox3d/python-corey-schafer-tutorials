#
#   https://www.youtube.com/watch?v=K8L6KVGG-7o
#
#################################################################################
import utils
import re
from collections import namedtuple
import os


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''
myemailre = r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)'
otheremailre = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

pattern = re.compile(otheremailre)

matches = pattern.finditer(emails)

for match in matches:
    print(match)

