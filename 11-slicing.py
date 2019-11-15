#
# https://www.youtube.com/watch?v=ajrtAuDg3yw
#
#################################################################################

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:stop]

# create indexes list to iterate
positive_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
negative_indexes = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
negative_indexes.reverse()

# show positive indexes formatted
for p in positive_indexes:
    print(f'{p:>3}', end='')
print()

# show negative indexes formatted
for n in negative_indexes:
    print(f'{n:>3}', end='')
print()
#################################################################################
print('#' * 80)
#################################################################################
#
#   loop over the two list of indexes simultaneously
#
for start, end in zip(positive_indexes, negative_indexes):
    #
    # always show the range
    #
    print(f'[{start:>3}:{end:>3}]', end='')
    #
    # if the range contains data
    #
    if len(my_list[start:end]):
        #
        # print offset in spaces
        #
        print(f'{"   " * start}', end='')
        #
        #   print all the matching elements formatted
        #
        for x in my_list[start:end]:
            print(f'{x:>3}', end='')
    print()
