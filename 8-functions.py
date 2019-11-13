#
# https://www.youtube.com/watch?v=9Os0o3wzS_I
#
#################################################################################


# simple hello function
def hello_func():
    print('hello from hello_func')


print(hello_func)
hello_func()


# function returning string
def hello_func():
    return 'hello from hello_func'


print(hello_func())
print(hello_func().upper())


# function returns strings and accept parameter
def hello_func(greeting):
    return '{} Function.'.format(greeting)


print(hello_func('hello'))


# function with positional argument and optional parameter with default value
def hello_func(greeting, name='you'):
    return '{}, {}.'.format(greeting, name)


print(hello_func('hello'))
print(hello_func('hello', 'robb'))


# function with optional positional arguments and optional keyword arguments
def student_info(*args, **kwargs):
    print('\nstudent_info')
    print(f'args   : {args}')
    print(f'kwargs : {kwargs}')


student_info('args1', 'args2', kwargs1=1, kwargs2=2)
#
#   unpacking parameters
#
courses = ['math', 'art']
info = {'name': 'robb', 'age': 40}
# not what we want:
# courses and info become two elements of the tuple args
student_info(courses, info)

# correct
student_info(*courses, **info)

