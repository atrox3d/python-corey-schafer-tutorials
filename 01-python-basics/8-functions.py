#
# https://www.youtube.com/watch?v=9Os0o3wzS_I
#
#################################################################################


def hello_func():
    """simple hello function"""
    print('hello from hello_func')


print(hello_func)
hello_func()


def hello_func():
    """function returning string"""
    return 'hello from hello_func'


print(hello_func())
print(hello_func().upper())


def hello_func(greeting):
    """function returns strings and accept parameter"""
    return '{} Function.'.format(greeting)


print(hello_func('hello'))


def hello_func(greeting, name='you'):
    """function with positional argument and optional parameter with default value"""
    return '{}, {}.'.format(greeting, name)


print(hello_func('hello'))
print(hello_func('hello', 'robb'))


def student_info(*args, **kwargs):
    """function with optional positional arguments and optional keyword arguments"""
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

