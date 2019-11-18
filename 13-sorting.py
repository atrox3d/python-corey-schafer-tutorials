#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
#################################################################################
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
sorted_li = sorted(li)
"""

simple string sorting

"""
print("#" * 80)
print('sorting non in-place')
print("#" * 80)
print(f'original list id({id(li)}) : {li}')
print(f'sorted() list id({id(sorted_li)}) : {sorted_li}')
print(f'----> ids are {"" if li is sorted_li else "not"} the same')
print()
print("#" * 80)
print('sorting in-place')
print("#" * 80)
print(f'original list  : {li}')
li.sort()
print(f'.sort() list   : {li}')
print("----> same variable")
