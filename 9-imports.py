#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
#################################################################################
# normal import
import module
# rename module
import module as m
# import some symbol
from module import find_index, test
# import and rename symbols
from module import find_index as fi, test
# import everything
from module import *

import sys

courses = ['history', 'math', 'physics', 'compsci']

# fully qualified name module
index = module.find_index(courses, 'math')
print(index)

# renamed module
index = m.find_index(courses, 'math')
print(index)

# just the function
index = find_index(courses, 'math')
print(index)

# renamed function
index = fi(courses, 'math')
print(index)

print(test)

print(f'sys.path = {sys.path}')
for path in sys.path:
    print(f'path = {path}')

print(f'module path: {module.__file__}')


