#
#   https://www.youtube.com/watch?v=5cvM-crlDvg
#
#   Python Tutorial: str() vs repr()
#
#################################################################################
from modules import utils

utils.banner(
    'https://www.youtube.com/watch?v=GfxJYp9_nJA',
    'str() vs repr()'
)

# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable

a = [1, 2, 3, 4]
b = 'sample string'

print(f'str(a) : {str(a)}')
print(f'str(b) : {str(b)}')
print()
print(f'repr(a): {repr(a)}')
print(f'repr(b): {repr(b)}')
print()
print(f'padded quoted f-string: {b!r:<20}x')

utils.banner('datetime example')
import datetime

dateobject = datetime.datetime.now()
datestr = str(dateobject)
daterepr = repr(dateobject)
print(f'dateobject : {dateobject}')
print(f'datestr    : {datestr}')
print(f'daterepr   : {daterepr}')
print()

dateeval = eval(daterepr)
dateevalstr = str(dateeval)
dateevalrepr = repr(dateeval)

print(f'dateeval       : {dateeval}')
print(f'dateevalstr    : {dateevalstr}')
print(f'dateevalrepr   : {dateevalrepr}')
print()

print('dateobject == dateeval  : ', dateobject == dateeval)
print('datestr == dateevalstr  : ', datestr == dateevalstr)
print('daterepr == dateevalrepr: ', dateobject == dateeval)


