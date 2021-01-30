#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
#################################################################################
print('Imported my_module.py')
print(f'Imported {__file__}')

test = 'Test String'


def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    #
    #   associate index to every element
    #
    for i, value in enumerate(to_search):
        #
        #   return index if value is found
        #
        if value == target:
            return i
    #
    #   return -1 if value not found
    #
    return -1


def double(n):
    """
    >>> double(2)
    4
    """
    return n * 2
