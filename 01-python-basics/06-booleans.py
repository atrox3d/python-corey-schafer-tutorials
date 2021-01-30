#
# https://www.youtube.com/watch?v=DZwmZ8Usvnk
#
# Python Tutorial for Beginners 6: Conditionals and Booleans - If, Else, and Elif Statements
#
#################################################################################
#
# equality and identity
#
a = [1, 2, 3]
b = [1, 2, 3]
#
print(f'a = {a}')                           # a = [1, 2, 3]
print(f'b = {b}')                           # b = [1, 2, 3]
#
print(f'equality: a == b : {a == b}')       # equality: a == b : True
print(f'identity: a is b : {a is b}')       # identity: a is b : False
print(f'id(a): {id(a)}')                    # id(a): 5316936
print(f'id(b): {id(b)}')                    # id(b): 5433416
#
# false values
#
false_values = [False, None, 0, '', "", list(), tuple(), set(), dict()]
print(f'false_values = {false_values}')     # false_values = [False, None, 0, '', '', [], (), set(), {}]
#
for val in false_values:
    if val:
        print(f'{val} is True')
    else:
        print(f'{val} is False')
            # False is False
            # None is False
            # 0 is False
            #  is False
            #  is False
            # [] is False
            # () is False
            # set() is False
            # {} is False
