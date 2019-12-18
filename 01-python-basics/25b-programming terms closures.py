#
#   https://www.youtube.com/watch?v=swU3c34d2NQ
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('closures: call inner function before returning its return value (None)')


def outer_func():
    #
    #   free variable
    #
    message = "hi"

    #
    #   define an inner function
    #
    def inner_func():
        print(f'inner_func: {message}')

    #
    #   returns None, after executing inner_func
    #
    return inner_func()


#
#   test this form of closure
#
x = outer_func()
utils.printfvar(x, 'x')

#################################################################################
utils.banner('closures: return the inner function without calling it')


#
#   redefine outer_func
#   this time returning the function inner_func without parenthesis, not its return value
#
def outer_func():
    #
    #   free variable
    #
    message = "hi"

    #
    #   define an inner function
    #
    def inner_func():
        print(f'inner_func, accessing outer message variable value: {message}')

    #
    #   returns None, after executing inner_func
    #
    return inner_func


#
#   test this form of closure
#
print()
my_func = outer_func()
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
    #
    #   free variable
    #
    message = msg

    #
    #   define an inner function
    #
    def inner_func():
        print(f'inner_func, accessing outer message argument value: {message}')

    #
    #   returns None, after executing inner_func
    #
    return inner_func


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

    def wrap(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap


#
#   test our closure
#
h1 = html('H1')
p = html('P')

h1('headline')
p('paragraph')
