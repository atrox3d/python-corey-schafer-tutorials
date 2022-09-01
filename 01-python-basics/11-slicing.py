#
# https://www.youtube.com/watch?v=ajrtAuDg3yw
#
# Python Tutorial: Slicing Lists and Strings
#
#################################################################################

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9     # POSITIVE INDEXES
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1     # NEGATIVE INDEXES
# syntax: list[start:end:step]
# where:
#       start: start index, positive or negative
#       end  : end index, positive or negative
#       step : takes each nth element

# create indexes list to iterate
positive_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
negative_indexes = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
negative_indexes.reverse()                              # [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
print('#' * 80)

#################################################################################
print(' ' * 9, end='')                                  # show positive indexes formatted
for p in positive_indexes:                              # OUTPUT |            0,  1,  2,  3,  4,  5,  6,  7,  8,  9,
    print(f'{p:>3},', end='')
print()

print(' ' * 9, end='')                                  # show negative indexes formatted
for n in negative_indexes:                              # OUTPUT |           -1, -2, -3, -4, -5, -6, -7, -8, -9,-10,
    print(f'{n:>3},', end='')
print()

print('#' * 80)

#################################################################################

# OUTPUT | [(0, -1), (1, -2), (2, -3), (3, -4), (4, -5), (5, -6), (6, -7), (7, -8), (8, -9), (9, -10)]
print(list(zip(positive_indexes, negative_indexes)))

for start, end in zip(
        positive_indexes, negative_indexes):            # loop over the two list of indexes simultaneously
    print(f'[{start:>3}:{end:>3}]', end='')             # always show the range
    if len(my_list[start:end]):                         # if the range contains data
        print(f'{"   ," * start}', end='')              # print offset in spaces
        for x in my_list[start:end]:                    # print all the matching elements formatted
            print(f'{x:>3},', end='')
    print()
#################################################################################
print('#' * 80)
#################################################################################
print(f'my_list : {my_list}')

for start in range(0, len(my_list)):                    # loop through list's elements
    for end in range(0, len(my_list)):                  # sub-loop through list's elements
        print(f'range[{start}:{end}] : ', end='')       # print current range
        print(f'{my_list[start:end]},', end='')         # print current slice
        print()
    print()
print()
