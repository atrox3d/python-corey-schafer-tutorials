#
# https://www.youtube.com/watch?v=9Os0o3wzS_I
#
# Python Tutorial for Beginners 8: Functions
#
#################################################################################
def hello_func():
    """
    simple hello function
    """
    print('hello from hello_func')                  # PRINTS string and returns


print(hello_func)                                   # OUTPUT | <function hello_func at 0x0034AAD8>
hello_func()                                        # OUTPUT | hello from hello_func


def hello_func():                                   # hello func with return
    """
    function returning string
    """
    return 'hello from hello_func'                  # RETURNS string


print(hello_func())                                 # OUTPUT | hello from hello_func
print(hello_func().upper())                         # OUTPUT | HELLO FROM HELLO_FUNC


def hello_func(greeting):                           # hello_func with return and format
    """
    function returns strings
    and accept parameter
    """
    #        +----------------------+
    #        |                      |
    return '{} Function.'.format(greeting)


print(hello_func('hello'))                          # OUTPUT | "hello Function."


def hello_func(greeting, name='you'):               # hello function with default param
    """
    function with positional argument
    and optional parameter
    with default value
    """
    #           +----------------------+
    #           |                      |
    #       +---+--------------+       |
    #       |   |              |       |
    return '{}, {}.'.format(greeting, name)


print(hello_func('hello'))                          # OUTPUT | hello, you.
print(hello_func('hello', 'robb'))                  # OUTPUT | hello, robb.


def student_info(
        *args,                                      # optional positional args
        **kwargs                                    # optional keyword args
):
    """
    function with optional positional
    arguments and optional keyword
    arguments
    """
    print('\nstudent_info')
    print(f'args   : {args}')                       # prints args tuple
    print(f'kwargs : {kwargs}')                     # prints kwargs dict


##################################################################################################
#
#
# direct approach, explicit specification of parameters
#
#
##################################################################################################
print(f"\n\ncall: student_info('args1', 'args2', kwargs1=1, kwargs2=2)")
student_info(                                       # OUTPUT | student_info
        'args1', 'args2',                           # OUTPUT | args   : ('args1', 'args2')
        kwargs1=1, kwargs2=2                        # OUTPUT | kwargs : {'kwargs1': 1, 'kwargs2': 2}
)


print(f"\n\ncall: student_info('math', 'art', name='robb', age=40)")
student_info(                                       # OUTPUT | student_info
        'math', 'art',                              # OUTPUT | args   : ('math', 'art')
        name='robb', age=40                         # OUTPUT | kwargs : {'name': 'robb', 'age': 40}
)
##################################################################################################
#
#   unpacking parameters
#
##################################################################################################
courses = ['math', 'art']                           # list
info = {'name': 'robb', 'age': 40}                  # dict
#
# not what we want:
# courses and info become two elements of the tuple args
#
print(f"\n\ncourses={courses}, info={info}")
print(f"call: student_info(courses, info")
student_info(courses, info)                         # OUTPUT | student_info
                                                    # OUTPUT | args   : (['math', 'art'], {'name': 'robb', 'age': 40})
                                                    # OUTPUT | kwargs : {}
#
# correct, unpacking
#
print(f"\n\ncourses={courses}, info={info}")
print(f"call: student_info(*courses, **info")
student_info(*courses, **info)                      # OUTPUT | student_info
                                                    # OUTPUT | args   : ('math', 'art')
                                                    # OUTPUT | kwargs : {'name': 'robb', 'age': 40}

