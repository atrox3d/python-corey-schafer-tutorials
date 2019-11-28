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

