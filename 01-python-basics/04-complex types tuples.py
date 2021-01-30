#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#
#################################################################################
#
# lists
#
"""
 list2 and list1 are the same list, so, if we modify one of them we get both modified
"""
list1 = ['history', 'math', 'physics', 'compsci']
list2 = list1

print(f'list1: {list1}')                # list1: ['history', 'math', 'physics', 'compsci']
print(f'list2: {list2}')                # list2: ['history', 'math', 'physics', 'compsci']

print("list1[0] = 'art'")
list1[0] = 'art'

print(f'list1: {list1}')                # list1: ['art', 'math', 'physics', 'compsci']
print(f'list2: {list2}')                # list2: ['art', 'math', 'physics', 'compsci']
#
# tuples
#
tuple1 = ('history', 'math', 'physics', 'compsci')
tuple2 = tuple1

print(f'tuple1: {tuple1}')              # tuple1: ('history', 'math', 'physics', 'compsci')
print(f'tuple2: {tuple2}')              # tuple2: ('history', 'math', 'physics', 'compsci')
#
#   tuples are immutable
#
try:
    print("tuple1[0] = 'art'")
    tuple1[0] = 'art'
except TypeError as te:
    print(f'Exception: {te}')           # Exception: 'tuple' object does not support item assignment

print(f'tuple1: {tuple1}')              # tuple1: ('history', 'math', 'physics', 'compsci')
print(f'tuple2: {tuple2}')              # tuple2: ('history', 'math', 'physics', 'compsci')
