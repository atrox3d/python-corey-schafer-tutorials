#
#   https://www.youtube.com/watch?v=K8L6KVGG-7o
#
#################################################################################
from modules import utils
import re
from collections import namedtuple
import os


def printresults(expression, description, count):
    """
    prints a formatted line with the search results stats
    """

    # helper, quotes string
    def quote(s): return f'"{s}"'

    print(f'results for {quote(expression):<20} ({description:<20}): ({count})')


def findregex(expression, description, text):
    """
    search for the expression inside text
    returns:
        - a namedtuple containing expression and description
        - match count
        - match object
    """
    regexd = dict(expression=expression, description=description)
    regex = namedtuple('regex', regexd.keys())(**regexd)
    # print(expression, description)
    pattern = re.compile(regex.expression)
    #
    # get a search results iterator
    #
    count = len(pattern.findall(text))
    matches = pattern.finditer(text)
    # def quote(s): return f'"{s}"'
    # print(f'results for {quote(regex.expression):<20} ({regex.description:<20}): ({count})')
    return regex, count, matches


text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890

Ha HaHa

MetaCharacters (Need to be escaped):

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = 'Start a sentence and then bring it to an end'

###############################################################################################
#
#
#
#
#   understanding raw strings
#
#
#
#
###############################################################################################
utils.banner('understanding raw strings')
print('normal strings: the \\t at the beginnig is interpreted into a tab char')
print('\tTab')

print('raw strings: prepending an r to the quotes r\'\' the \\t at the beginnig is NOT interpreted into a tab char')
print(r'\tTab')
###############################################################################################
#
#
#
#
#   simple regular expressions
#
#
#
#
###############################################################################################
utils.banner('simple regular expressions')
print("text to search:")
utils.hashline(char='-')
print(text_to_search, end='')
utils.hashline(char='-')

for regex in [
    dict(
        expression=r'abc',
        description='normal text'
    ),
    dict(
        expression=r'\.',
        description='actual dot'
    ),
    dict(
        expression=r'.',
        description='any character'
    ),
    dict(
        expression=r'coreyms\.com',
        description='url'
    ),
    dict(
        expression=r'\d',
        description='digit'
    ),
    dict(
        expression=r'\D',
        description='non digit'
    ),
    dict(
        expression=r'\w',
        description='word character'
    ),
    dict(
        expression=r'\W',
        description='non word character'
    ),
    dict(
        expression=r'\s',
        description='whitespace'
    ),
    dict(
        expression=r'\S',
        description='non whitespace'
    ),
    dict(
        expression=r'\bHa',
        description='word bounbary before'
    ),
    dict(
        expression=r'\BHa',
        description='no word bounbary before'
    ),
    dict(
        expression=r'\bHa\b',
        description='word bounbaries'
    ),
]:
    regex, count, matches = findregex(**regex, text=text_to_search)

    printresults(regex.expression, regex.description, count)

    utils.hashline(char='-')
    # for match in matches:
    #     # <re.Match object; span=(1, 4), match='abc'>
    #     print('match object                      :', match)
    #     # print('slicing text using span=(1, 4):', text_to_search[1:4])
    #     print('slicing text using span=({:>3}, {:>3}): "{}"'.format(
    #                                                             match.start(),
    #                                                             match.end(),
    #                                                             text_to_search[match.start():match.end()]
    #                                                 )
    #          )
    # utils.hashline(char='-')

utils.banner('search with anchors')
print("text to search:")
utils.hashline(char='-')
print(sentence)
utils.hashline(char='-')

for regex in [
    dict(
        expression=r'^Start',
        description='^anchor'
    ),
    dict(
        expression=r'end$',
        description='anchor$'
    ),
]:
    regex, count, matches = findregex(**regex, text=sentence)
    printresults(regex.expression, regex.description,count)

    utils.hashline(char='-')

###############################################################################################
#
#
#
#
#   easy regular expressions
#
#
#
#
###############################################################################################
utils.banner('easy regular expressions')
print("text to search:")
utils.hashline(char='-')
print(text_to_search, end='')
utils.hashline(char='-')

regex = dict(
                expression = r'\d\d\d.\d\d\d.\d\d\d\d',
                description = 'phone number',
)
# pattern = re.compile(expression)
#
# get a search results iterator
#
# count = len(pattern.findall(text_to_search))
# matches = pattern.finditer(text_to_search)
regex, count, matches = findregex(**regex, text=text_to_search)

printresults(regex.expression, regex.description, count)

utils.hashline(char='-')
for match in matches:
    print(match)
utils.hashline(char='-')
###############################################################################################
#
#
#
#
#   search inside file
#
#
#
#
###############################################################################################
utils.banner('search inside file')
datafilepath = os.path.join(os.getcwd(), '..', 'data', 'data.txt')

with open(datafilepath, 'r') as datafile:
    expression = r'\d\d\d.\d\d\d.\d\d\d\d'
    description = 'phone number'
    contents = datafile.read()
    regex, count, matches = findregex(expression, description, text=contents)

    printresults(regex.expression, regex.description, count)

    utils.hashline(char='-')
    for match in matches:
        print(match)

###############################################################################################
#
#
#
#
#   sets, quantifiers and groups
#
#
#
#
###############################################################################################
utils.banner('sets, quantifiers and groups')

expression = r'(Mr|MS|Mrs)'     # group
expression += r'\.?'            # quantifier
expression += r'\s'             # space
expression += r'[A-Z]'          # set
expression += r'\w*'            # quantifier

expression = r'(Mr|MS|Mrs)\.?\s[A-Z]\w*'
description = 'sets, quantifiers and groups'

regex, count, matches = findregex(expression, description, text=text_to_search)
printresults(regex.expression, regex.description, count)
utils.hashline(char='-')
for match in matches:
    print(match)
