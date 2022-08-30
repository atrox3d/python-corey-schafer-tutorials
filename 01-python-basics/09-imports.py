#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
# Python Tutorial for Beginners 9: Import Modules and Exploring The Standard Library
#
#################################################################################
#
from modules import module                          # normal import
from modules import module as m                     # rename module
#
from modules.module import find_index as fi         # import and rename symbol
#
from modules.module import *                        # import everything
#
import sys


def foundat(index):
    return f'math {"found at " + str(index) if index >= 0 else "not found"}'


courses = ['history', 'math', 'physics', 'compsci']
print(f"courses = {courses}")
#
index = module.find_index(courses, 'math')          # fully qualified name module
print(foundat(index))
#
index = m.find_index(courses, 'math')               # renamed module
print(foundat(index))
#
index = find_index(courses, 'math')                 # just the function
print(foundat(index))
#
index = fi(courses, 'math')                         # renamed function
print(foundat(index))
#
print(test)                                         # print module symbol
#
print(f'sys.path = {sys.path}')                     # print all syspath
for path in sys.path:                               # print each element
    print(f'path = {path}')

print(f'module path: {module.__file__}')


