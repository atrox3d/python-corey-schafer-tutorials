#
# https://www.youtube.com/watch?v=vTX3IwquFkc
#
# Python Tutorial: String Formatting - Advanced Operations for Dicts, Lists, Numbers, and Dates
#
#################################################################################
person = {'name': 'john', 'age': 23}
#
#   unformatted strings
#
sentence = 'my name is ' + person['name'] + ' and i am ' + str(person['age']) + ' years old.'
print(sentence)
#
#   .format placeholder
#
sentence = 'my name is {} and i am {} years old'.format(person['name'], person['age'])
print(sentence)
#
#   .format with indexes
#
tag = 'h1'
text = 'this is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)

#
#   .format with subscript
#
sentence = 'my name is {0} and i am {1} years old'.format(person['name'], person['age'])
print(sentence)
sentence = 'my name is {0[name]} and i am {1[age]} years old'.format(person, person)
print(sentence)
sentence = 'my name is {0[name]} and i am {0[age]} years old'.format(person)
print(sentence)
sentence = 'my name is {0[0]} and i am {0[1]} years old'.format(list(person.values()))
print(sentence)


#
#   .format class members
#
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


personobj = Person('jack', 40)
sentence = 'my name is {0.name} and i am {0.age} years old'.format(personobj)
print(sentence)
#
#   .format keyword arguments
#
sentence = 'my name is {name} and i am {age} years old'.format(name='joe', age=35)
print(sentence)
#
#   .format dictionaries with keyword arguments unpack
#
sentence = 'my name is {name} and i am {age} years old'.format(**person)
print(sentence)
"""


custom placeholder formatting


"""
for i in range(1, 6):
    # no formatting
    sentence = 'the value of i is {}'.format(i)
    print(sentence)
    # zero padding
    sentence = 'the value of i is {:02}'.format(i)
    print(sentence)
    sentence = 'the value of i is {:03}'.format(i)
    print(sentence)
#
#   decimal formatting
#
from math import pi

sentence = 'PI is equal to {}'.format(pi)
print(sentence)
sentence = 'PI is equal to {:.2f}'.format(pi)
print(sentence)
#
#   big numbers formatting
#
sentence = '1 MB is equal to {} bytes'.format(1000 ** 2)
print(sentence)
sentence = '1 MB is equal to {:,} bytes'.format(1000 ** 2)
print(sentence)
sentence = '1 MB is equal to {:,.2f} bytes'.format(1000 ** 2)
print(sentence)
#
#   datetime formatting
#
#   https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
#
import datetime

mydate = datetime.datetime(2019, 11, 18, 15, 30, 00)
print(mydate)
sentence = '{:%B %d, %Y}'.format(mydate)
print(sentence)
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(mydate)
print(sentence)

