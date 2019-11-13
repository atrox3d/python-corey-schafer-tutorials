#
# https://www.youtube.com/watch?v=6iF8Xb7Z3wQ
#
#################################################################################
#
# for loops
#
nums = list(range(1, 6))
print(nums)

print('\nloop with break')
for num in nums:
    if num == 3:
        print('found, break')
        break
    print(num)

print('\nloop with continue')
for num in nums:
    if num == 3:
        print('found, continue')
        continue
    print(num)

print('\ninner loop')
for num in nums:
    for letter in 'abc':
        print(num, letter)

print('\nrange loop')
for num in range(10):
    print(num)

#
# while loops
#
