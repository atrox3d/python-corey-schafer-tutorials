#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
#################################################################################


def print_sortedlist(banner_title, original_list, sorted_list):
    print("#" * 80)
    print(banner_title)
    print("#" * 80)
    print(f'original list id({id(original_list)}) : {original_list}')
    print(f'sorted() list id({id(sorted_list)}) : {sorted_list}')
    print(f'----> ids are {"" if original_list is sorted_list else "not"} the same')
    print()


def print_list_sort(banner_title, original_list, sorted_list):
    print("#" * 80)
    print(banner_title)
    print("#" * 80)
    print(f'original list : {original_list}')
    print(f'.sort()  list : {sorted_list}')
    print()


li = [9, 1, 8, 2, 7, 3, 6, 4, 5]
"""

simple string sorting

"""
sorted_li = sorted(li)
print_sortedlist('sorting non in-place', li, sorted_li)
#
original_list = li.copy()
li.sort()
print_list_sort("sorting in-place", original_list, li)
"""


reverse string sort


"""
li = original_list
reverse_li = sorted(li, reverse=True)
print_sortedlist('reverse sorting non in-place', li, reverse_li)
#
original_list = li.copy()
li.sort(reverse=True)
print_list_sort("reverse sorting in-place", original_list, li)
