#
# https://www.youtube.com/watch?v=k9TUPpGqYTo
#
#################################################################################
# string
message = 'Hello World'
# string length
print(len(message))
# string index
print(message[0])
# string index error
try:
    print(message[11])
except IndexError as ie:
    print(ie)
# slicing
print(message[0:5])
print(message[:5])
print(message[6:])
#
# string methods
#
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

new_message = message.replace('World', 'Universe')
print(new_message)
print(message)
# string concatenation
greeting = 'Hello'
name = 'Michael'

message = greeting + name
print(message)

message = greeting + ', ' + name + '. Welcome!'
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
#
# dir, help
#
print(dir(name))
print(help(str))
print(help(str.lower))
