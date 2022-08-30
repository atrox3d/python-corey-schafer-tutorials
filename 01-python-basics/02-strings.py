#
# https://www.youtube.com/watch?v=k9TUPpGqYTo
#
# Python Tutorial for Beginners 2: Strings - Working with Textual Data
#
#################################################################################
#
# string
#
message = 'Hello World'
#
# string length
#
print(len(message))                 # 11
#
# string index
#
print(message[0])                   # H
#
# string index error
#
try:
    print(message[11])
except IndexError as ie:
    print(ie)                       # string index out of range
#
# slicing
#
                                    # size      12345
                                    # string    Hello World
                                    # index     0123456789
print(message[0:5])                 # Hello
print(message[:5])                  # Hello
print(message[6:])                  # World
#
# string methods
#
print(message.lower())              # hello world
print(message.count('Hello'))       # 1
print(message.count('l'))           # 3
print(message.find('World'))        # 6
print(message.find('Universe'))     # -1
#
# create new string object
#
new_message = message.replace('World', 'Universe')
print(new_message)                  # Hello Universe
print(message)                      # Hello World
#
# string concatenation
#
greeting = 'Hello'
name = 'Michael'
#
# base concatenation
#
message = greeting + name
print(message)                      # HelloMichael
#
message = greeting + ', ' + name + '. Welcome!'
print(message)                      # Hello, Michael. Welcome!
#
# str format method
#
#               +------------------------------+
#               |                              |
#           +---+----------------------+       |
#           |   |                      |       |
message = '{}, {}. Welcome!'.format(greeting, name)     # positional {} substitution
print(message)                                          # Hello, Michael. Welcome!
#
# f strings
#
message = f'{greeting}, {name.upper()}. Welcome!'       # direct expression evaluation
print(message)                                          # Hello, MICHAEL. Welcome!
#
# dir, help
#
print(dir(name))
print(help(str))
print(help(str.lower))
