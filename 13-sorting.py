#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
#################################################################################
li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
s_li = sorted(li)

print("#" * 80)
print('sorting non in-place')
print("#" * 80)
print(f'original list id({id(li)}) : {li}')
print(f'sorted() list id({id(s_li)}) : {s_li}')
print(f'----> ids are {"" if li is s_li else "not"} the same')
print()
print("#" * 80)
print('sorting in-place')
print("#" * 80)
print(f'original list  : {li}')
li.sort()
print(f'.sort() list   : {li}')
print("----> same variable")
