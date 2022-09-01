#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
# Python Tutorial: Sorting Lists, Tuples, and Objects
#
#################################################################################


def same(list1, list2):
    if list1 is list2:
        return ""
    else:
        return "not"


def print_sortedlist(banner_title, original_list, sorted_list):
    print("#" * 80)
    print(banner_title)
    print("#" * 80)

    print(
        f'original list '
        f'id({id(original_list)}) : '
        f'{original_list}'
    )

    print(
        f'sorted() list '
        f'id({id(sorted_list)}) : '
        f'{sorted_list}'
    )

    print(
        f'----> ids are '
        f'{same(original_list, sorted_list)}'
        f' the same'
    )
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


simple list sorting


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
"""


complex list sorting


"""
nums = [-6, -5, -4, 1, 2, 3]

sorted_nums = sorted(nums)
print_sortedlist("sort signed integers", nums, sorted_nums)

sorted_abs = sorted(nums, key=abs)
print_sortedlist("sort absolute values of signed integers", nums, sorted_abs)
