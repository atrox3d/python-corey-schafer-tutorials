#
# https://www.youtube.com/watch?v=ajrtAuDg3yw
#
#################################################################################

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1
# list[start:end:stop]

positive_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
negative_indexes = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
negative_indexes.reverse()

for p in positive_indexes:
    print(f'{p:>3}', end='')
print()

for n in negative_indexes:
    print(f'{n:>3}', end='')
print()

for start, end in zip(positive_indexes, negative_indexes):
    #print(f'{start:>3}:{end:>3}')
    if my_list[start:end]:
        print(f'[{start:>3}:{end:>3}]{" " * start}{my_list[start:end]}')
    else:
        print(f'[{start:>3}:{end:>3}]')

# for x in range(0, len(my_list)):
#     print(f'my_list[{x}] : {my_list[x]}')

# for x in range(0, len(my_list)):
#     for l in range(0, len(my_list)):
#         print(f'my_list[{x}:{l}] : {my_list[x:l]}')

# for x in range(0, len(my_list)):
#     print(f'my_list[x,y] : {my_list}')
#     print(f'my_list[{x}:{x+3}] : {my_list[x:x+3]}')
