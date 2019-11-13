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

print(list1)
print(list2)

list1[0] = 'art'

print(list1)
print(list2)

# tuples
"""
"""
tuple1 = ('history', 'math', 'physics', 'compsci')
tuple2 = tuple1

print(tuple1)
print(tuple2)

try:
    tuple1[0] = 'art'
except TypeError as te:
    print(f'Exception: {te}')

print(tuple1)
print(tuple2)

