#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
#################################################################################
# lists
"""
 list2 and list1 are the same list, so, if we modify one of them we get both modified
"""
list1 = ['history', 'math', 'physics', 'compsci']
list2 = list1

print(f'list1: {list1}')
print(f'list2: {list2}')

print("list1[0] = 'art'")
list1[0] = 'art'

print(f'list1: {list1}')
print(f'list2: {list2}')

# tuples
"""
"""
tuple1 = ('history', 'math', 'physics', 'compsci')
tuple2 = tuple1

print(f'tuple1: {tuple1}')
print(f'tuple2: {tuple2}')

try:
    print("tuple1[0] = 'art'")
    tuple1[0] = 'art'
except TypeError as te:
    print(f'Exception: {te}')

print(f'tuple1: {tuple1}')
print(f'tuple2: {tuple2}')

