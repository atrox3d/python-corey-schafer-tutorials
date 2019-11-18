#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
#################################################################################


def print_sortedobj(banner_title, original_obj, sorted_obj):
    print("#" * 80)
    print(banner_title)
    print("#" * 80)
    print(f'original <{original_obj.__class__.__name__}> : {original_obj}')
    print(f'sorted() <{sorted_obj.__class__.__name__}> : {sorted_obj}')
    print('----> sorted() always returns a list')
    print()


"""


tuples


"""
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
try:
    tup.sort()
except AttributeError as ae:
    print(f'cannot call .sort on a {tup.__class__.__name__} : ', ae)

sorted_tuple = sorted(tup)
print_sortedobj("sorted tuple", tup, sorted_tuple)

"""


dictionaries


"""
di = {
    'name': 'robb',
    'job': 'programmer',
    'age': None,
    'os': 'winshit'
}

try:
    di.sort()
except AttributeError as ae:
    print(f'cannot call .sort of a {di.__class__.__name__} : ', ae)

sorted_di = sorted(di)
print_sortedobj("sorted dict", di, sorted_di)

