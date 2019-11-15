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
my_list = [n for n in nums if not n % 2]
print("\ngenerate sublist of even elements from nums to my_list, list comprehension: [n for n in nums if not n%2]")
print(f'{"my_list":<10} = {my_list}')
# map + lambda version
my_list = list(filter(lambda n: n % 2 == 0, nums))
print("\ngenerate list of squares of nums in my_list, filter + lambda: filter(lambda n: n % 2 == 0, nums)")
print(f'{"my_list":<10} = {my_list}')
"""
generate a list of letter, num pairs for each element of abcd 0123
"""
print("#" * 80)
# for loop version
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print("\ngenerate a list of letter, num pairs for each element of abcd 0123, for loop:")
print(f'{"my_list":<10} = {my_list}')
# list comprehension version
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
print(
    "\ngenerate a list of letter, num pairs for each element of abcd 0123, list comprehension: [n for n in nums if not n%2]")
print(f'{"my_list":<10} = {my_list}')
"""
generate a dictionary of civilian names of superheroes 
"""
print("#" * 80)
names = ['bruce', 'clark', 'peter', 'logan', 'wade']
heroes = ['batman', 'superman', 'spiderman', 'wolverine', 'deadpool']
print(f'{"names":<10} = {names}')
print(f'{"heroes":<10} = {heroes}')
# for loop version
my_dict = {}
for name, hero in zip(names, heroes):
    my_dict[name] = hero
print("\ngenerate a dictionary of civilian names of superheroes, for loop:")
print(f'{"my_dict":<10} = {my_dict}')
# dictionary comprehension version
my_dict = {name: hero for name, hero in zip(names, heroes)}
print(
    "\ngenerate a dictionary of civilian names of superheroes, list comprehension: {name: hero for name, hero in zip(names, heroes)}")
print(f'{"my_dict":<10} = {my_dict}')
# conditional dictionary comprehension version
my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'peter'}
print(
    "\ngenerate a dictionary of civilian names of superheroes, list comprehension: {name: hero for name, hero in zip(names, heroes) if name != 'peter'}")
print(f'{"my_dict":<10} = {my_dict}')
"""
generate a set 
"""
print("#" * 80)
nums = [1, 2, 3, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
print(f'{"nums":<10} = {nums}')
# for loop version
my_set = set()
for n in nums:
    my_set.add(n)
print("\ngenerate a set of unique numbers from a list, for loop:")
print(f'{"my_set":<10} = {my_set}')
# set comprehension version
my_set = {n for n in nums}
print("\ngenerate a set of unique numbers from a list, set comprehension: {n for n in nums}")
print(f'{"my_set":<10} = {my_set}')
# # conditional dictionary comprehension version
# my_dict = {name: hero for name, hero in zip(names, heroes) if name != 'peter'}
# print("\ngenerate a dictionary of civilian names of superheroes, list comprehension: {name: hero for name, hero in zip(names, heroes) if name != 'peter'}")
# print(f'{"my_dict":<10} = {my_dict}')
