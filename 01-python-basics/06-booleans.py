#
# https://www.youtube.com/watch?v=DZwmZ8Usvnk
#
#################################################################################

# equality and identity

a = [1, 2, 3]
b = [1, 2, 3]

print(f'a = {a}')
print(f'b = {b}')

print(f'equality: a == b : {a == b}')
print(f'identity: a is b : {a is b}')
print(f'id(a): {id(a)}')
print(f'id(b): {id(b)}')

# false values

false_values = [False, None, 0, '', "", list(), tuple(), set(), dict()]
print(f'false_values = {false_values}')

for val in false_values:
    if val:
        print(f'{val} is True')
    else:
        print(f'{val} is False')


