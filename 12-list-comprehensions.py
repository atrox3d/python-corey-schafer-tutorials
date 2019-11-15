#
# https://www.youtube.com/watch?v=3dt4OGnU5sM
#
#################################################################################
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'{"nums":<10} = {nums}')
"""
    copy list
"""
# for loop version
my_list = []
for n in nums:
    my_list.append(n)
print("\ncopy nums in my_list, for loop:")
print(f'{"my_list":<10} = {my_list}')
# list comprehension version
my_list = [n for n in nums]
print("\ncopy nums in my_list, list comprehension: [n for n in nums]")
print(f'{"my_list":<10} = {my_list}')
"""
    generate list of squares of n
"""
print("#" * 80)
# for loop version
my_list = []
for n in nums:
    my_list.append(n * n)
print("\ngenerate list of squares of nums in my_list, for loop:")
print(f'{"my_list":<10} = {my_list}')
# list comprehension version
my_list = [n * n for n in nums]
print("\ngenerate list of squares of nums in my_list, list comprehension: [n*n for n in nums]")
print(f'{"my_list":<10} = {my_list}')
# map + lambda version
my_list = list(map(lambda n: n * n, nums))
print("\ngenerate list of squares of nums in my_list, map + lambda: map(lambda n: n*n, nums)")
print(f'{"my_list":<10} = {my_list}')
"""
conditional list copy
"""
print("#" * 80)
# for loop version
my_list = []
for n in nums:
    if not n % 2:
        my_list.append(n)
print("\ngenerate sublist of even elements from nums to my_list, for loop:")
print(f'{"my_list":<10} = {my_list}')
# list comprehension version
my_list = [n for n in nums if not n%2]
print("\ngenerate sublist of even elements from nums to my_list, list comprehension: [n for n in nums if not n%2]")
print(f'{"my_list":<10} = {my_list}')
# map + lambda version
my_list = list(filter(lambda n: n % 2 == 0, nums))
print("\ngenerate list of squares of nums in my_list, filter + lambda: filter(lambda n: n % 2 == 0, nums)")
print(f'{"my_list":<10} = {my_list}')
