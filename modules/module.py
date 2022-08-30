#
# https://www.youtube.com/watch?v=CqvZ3vGoGs0
#
#################################################################################
print('Imported my_module.py')
print(f'Imported {__file__}')

test = 'Test String'


def find_index(to_search, target):
    """
    Find the index of a value in a sequence
    """
    for i, value in enumerate(to_search):           # associate index to every element
        if value == target:                         # return index if value is found
            return i

    return -1                                       # return -1 if value not found


def double(n):
    """
    :returns n * 2
    >>> double(5)
    10
    """
    return n * 2
