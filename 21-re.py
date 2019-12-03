#
#   https://www.youtube.com/watch?v=K8L6KVGG-7o
#
#################################################################################
import utils
import re

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
#   understanding raw strings
#
###############################################################################################
utils.banner('understanding raw strings')
print('normal strings: the \\t at the beginnig is interpreted into a tab char')
print('\tTab')

print('raw strings: prepending an r to the quotes r\'\' the \\t at the beginnig is NOT interpreted into a tab char')
print(r'\tTab')
###############################################################################################
#
#   regular expressions
#
###############################################################################################
utils.banner('regular expressions')
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
]:
    #
    # compile regexp pattern into a regexp object
    #
    # print(regex, type(regex));exit()
    expression = regex['expression']
    description = regex['description']
    pattern = re.compile(expression)
    #
    # get a search results iterator
    #
    count = len(pattern.findall(text_to_search))
    matches = pattern.finditer(text_to_search)
    print(f'results for {expression:<20} ({description:<20}): ({count})')
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
