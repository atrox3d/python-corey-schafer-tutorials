from modules import utils

########################################################################################################################
utils.banner(
    'https://dev.to/apcelent/python-decorator-tutorial-with-example-529f',
    'simple nested function'
)


def outer_function():
    print("1. This is outer function!")

    def inner_function():
        print("2. This is inner function, inside outer function!")

    print("3. This is outside inner function, inside outer function!")
    return inner_function()


func_assign = outer_function()
utils.printfvar(func_assign, 'func_assign')

########################################################################################################################
utils.banner("""
    Python decorator are the function that receive a function as an argument 
    and return another function as return value. 
    The assumption for a decorator is that we will pass a function as argument 
    and the signature of the inner function in the decorator must match the function to decorate.
""")

########################################################################################################################
utils.banner('')

"""
https://stackoverflow.com/questions/15624801/passing-a-parameter-to-the-decorator-in-python

Think about it this way: Before you even get to decorating test2, 
you're calling decAny('xxx'). 
But decAny takes a function, f0, not a string. So clearly at some point, 
that f0() is going to try to call 'xxx'.
"""

"""
https://realpython.com/primer-on-python-decorators/
"""

# outer_function
import functools


def dec(f):
    print(f'define w')

    #@functools.wraps(f)
    def w(*args, **kwargs):
        print(f'\tbefore: {f.__name__}({args}, {kwargs})')
        result = f(*args, **kwargs)
        print(f'\tafter : {f.__name__}({args}, {kwargs})')
        # print()
        return result

    return w


@dec
def hello():
    print()
    print('\t\thello')
    print()


hello = dec(hello)
hello = dec(hello)
hello = dec(hello)

hello()


