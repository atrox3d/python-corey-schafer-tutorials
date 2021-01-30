#
# https://www.youtube.com/watch?v=9Os0o3wzS_I
#
# Python Tutorial for Beginners 8: Functions
#
#################################################################################
#
#
#
def hello_func():
    """simple hello function"""
    print('hello from hello_func')


print(hello_func)                   # <function hello_func at 0x0034AAD8>
hello_func()                        # hello from hello_func
#
#
#
def hello_func():
    """function returning string"""
    return 'hello from hello_func'


print(hello_func())                 # hello from hello_func
print(hello_func().upper())         # HELLO FROM HELLO_FUNC
#
#
#
def hello_func(greeting):
    """function returns strings and accept parameter"""
    return '{} Function.'.format(greeting)


print(hello_func('hello'))          # hello Function.
#
#
#
def hello_func(greeting, name='you'):
    """function with positional argument and optional parameter with default value"""
    return '{}, {}.'.format(greeting, name)


print(hello_func('hello'))          # hello, you.
print(hello_func('hello', 'robb'))  # hello, robb.
#
#
#
def student_info(*args, **kwargs):
    """function with optional positional arguments and optional keyword arguments"""
    print('\nstudent_info')
    print(f'args   : {args}')
    print(f'kwargs : {kwargs}')


student_info('args1', 'args2', kwargs1=1, kwargs2=2)
                                    # student_info
                                    # args   : ('args1', 'args2')
                                    # kwargs : {'kwargs1': 1, 'kwargs2': 2}
#
#   unpacking parameters
#
courses = ['math', 'art']
info = {'name': 'robb', 'age': 40}
#
# not what we want:
# courses and info become two elements of the tuple args
#
student_info(courses, info)
                                    # student_info
                                    # args   : (['math', 'art'], {'name': 'robb', 'age': 40})
                                    # kwargs : {}
#
# correct, unpacking
#
student_info(*courses, **info)
                                    # student_info
                                    # args   : ('math', 'art')
                                    # kwargs : {'name': 'robb', 'age': 40}

