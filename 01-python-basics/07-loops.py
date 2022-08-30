#
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
#
# Python Tutorial for Beginners 7: Loops and Iterations - For/While Loops
#
#################################################################################
#
# for loops
#
nums = list(range(1, 6))
print(nums)                                 # [1, 2, 3, 4, 5]

print('\nloop with break')
for num in nums:                            # loop through [1, 2 , 3, 4, 5]
    if num == 3:
        print('found, break (no else)')
        break                               # break: else is not executed
    print(num)                              # only printed if num != 3
else:                                       # no break
    print("else")                           # only printed if 3 not in nums

print('\nloop with continue')
for num in nums:                            # loop through [1, 2 , 3, 4, 5]
    if num == 3:
        print('found, continue')
        continue                            # continue: else is executed
    print(num)                              # only printed if num != 3
else:                                       # no break
    print("else")                           # always printed

print('\ninner loop')
for num in nums:                            # loops through [1, 2, 3, 4, 5]
    for letter in 'abc':                    # sub loop through ['a', 'b', 'c']
        print(num, letter)                  # 1 a
                                            # 1 b
                                            # 1 c
                                            # 2 a
                                            # ...
else:                                       # no break
    print("else")                           # always printed, no break

print('\nrange loop')
for num in range(10):                       # loops thorugh [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(num)                              # 1
                                            # 2
                                            # ...
else:                                       # no break
    print("else")                           # always printed, no break

#
# while loops
#
print('\nwhile loop')
x = 0
while x < 10:                               # loops while x < 10
    print(x)
    x += 1                                  # x++
else:                                       # no break
    print("else")                           # always printed
