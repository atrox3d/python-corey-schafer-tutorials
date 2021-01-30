#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
# Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library
#
#################################################################################
#
# normal import
# rename module
#
from modules import module, module as m
#
# import some symbol
# import and rename symbols
#
from modules.module import find_index as fi
#
# import everything
#
from modules.module import *

import sys

courses = ['history', 'math', 'physics', 'compsci']
print(f"courses = {courses}")
#
# fully qualified name module
#
index = module.find_index(courses, 'math')
print(f'math {"found at " + str(index) if index >= 0 else "not found"}')
#
# renamed module
#
index = m.find_index(courses, 'math')
print(f'math {"found at " + str(index) if index >= 0 else "not found"}')
#
# just the function
#
index = find_index(courses, 'math')
print(f'math {"found at " + str(index) if index >= 0 else "not found"}')
#
# renamed function
#
index = fi(courses, 'math')
print(f'math {"found at " + str(index) if index >= 0 else "not found"}')
#
#   print module symbol
#
print(test)

print(f'sys.path = {sys.path}')

for path in sys.path:
    print(f'path = {path}')

print(f'module path: {module.__file__}')


