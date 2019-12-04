#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
#################################################################################
# normal import
from modules import module, module as m
# rename module
# import some symbol
# import and rename symbols
from modules.module import find_index as fi
# import everything
from modules.module import *

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


