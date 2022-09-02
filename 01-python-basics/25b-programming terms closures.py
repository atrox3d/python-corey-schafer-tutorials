#
#   https://www.youtube.com/watch?v=swU3c34d2NQ
#
#   Programming Terms: Closures - How to Use Them and Why They Are Useful
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('closures: call inner function before returning its return value (None)')


def outer_func():
    message = "hi"                                      # free variable

    def inner_func():                                   # define an inner function
        print(f'inner_func: {message}')

    return inner_func()                                 # returns None, after executing inner_func


x = outer_func()                                        # test this form of closure
utils.printfvar(x, 'x')

#################################################################################
utils.banner('closures: return the inner function without calling it')


#
#   redefine outer_func
#   this time returning the function inner_func
#   without parenthesis, not its return value
#
def outer_func():
    message = "hi"                                      # free variable

    def inner_func():                                   # define an inner function
        print(
            f'inner_func, '
            f'accessing outer message variable '        # print value of enclosing
            f'value: {message}'                         # variable message
        )

    return inner_func                                   # returns inner_func object


#
#   test this form of closure
#
print()
my_func = outer_func()                                  # my_func is now inner_func
utils.printfvar(my_func, my_func.__name__)
#
#   execute inner_func
#
my_func()
my_func()
my_func()
#################################################################################
utils.banner('closures: return the inner function without calling it and passing a parameter during creation')


#
#   redefine outer_func
#   this time we pass an argument during the creation of inner_func
#
def outer_func(msg):
    message = msg                                      # save parameter

    def inner_func():                                   # define an inner function
        print(
            f'inner_func, '
            f'accessing outer message variable '        # print value of enclosing
            f'value: {message}'                         # variable message
        )

    return inner_func                                   # returns inner_func object


#
#   test this form of closure
#
print()
hi = outer_func('hi')
hello = outer_func('hello')
hi()
hello()
#################################################################################
utils.banner(
    'closures: return the inner function without calling it and passing a parameter during creation and at call time')


#
#   parametric closure
#
def html(tag):
    print(f'creating wrap(): <{tag}>{{msg}}</{tag}>')

    def wrap(msg):                                      # will accept msg param
        print(f'<{tag}>{msg}</{tag}>')                  # saves tag parameter

    return wrap                                         # returns wrap function


#
#   test our closure
#
h1 = html('H1')
p = html('P')

h1('headline')
p('paragraph')
