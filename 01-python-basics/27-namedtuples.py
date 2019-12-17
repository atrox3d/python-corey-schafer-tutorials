#
#   https://www.youtube.com/watch?v=GfxJYp9_nJA
#
#################################################################################
from modules import utils
from collections import namedtuple

utils.banner(
    'https://www.youtube.com/watch?v=GfxJYp9_nJA',
    'named tuples'
)

tuple_colorwhite = (255, 255, 255)
print('rgb as tuple')
print(tuple_colorwhite)
print('red:', tuple_colorwhite[0])
print()

dict_colorwhite = dict(red=255, green=255, blue=255)
# or
dict_colorwhite = {'red': 255, 'green': 255, 'blue': 255}
print('rgb as dict')
print(dict_colorwhite)
print('red:', dict_colorwhite['red'])
print()

Color = namedtuple('Color', ['red', 'green', 'blue'])
namedtuple_colorwhite = Color(255, 255, 255)
# or
namedtuple_colorwhite = Color(red=255, green=255, blue=255)
print('rgb as namedtuple')
print(namedtuple_colorwhite)
print('red:', namedtuple_colorwhite.red)






