#
# https://www.youtube.com/watch?v=ajrtAuDg3yw
#
# Python Tutorial: Slicing Lists and Strings
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

#################################################################################
print('#' * 80)
#################################################################################
# show positive indexes formatted
print(' ' * 9, end='')
for p in positive_indexes:
    print(f'{p:>3},', end='')
print()

# show negative indexes formatted
print(' ' * 9, end='')
for n in negative_indexes:
    print(f'{n:>3},', end='')
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
        print(f'{"   ," * start}', end='')
        #
        #   print all the matching elements formatted
        #
        for x in my_list[start:end]:
            print(f'{x:>3},', end='')
    print()
#################################################################################
print('#' * 80)
#################################################################################
print(f'my_list : {my_list}')
# for x in range(0, len(my_list)):
#     print(f'{my_list[x]:>3},', end='')
# print()

for start in range(0, len(my_list)):
    for end in range(0, len(my_list)):
        print(f'range[{start}:{end}] : ', end='')
        print(f'{my_list[start:end]},', end='')
        print()
    print()
print()
