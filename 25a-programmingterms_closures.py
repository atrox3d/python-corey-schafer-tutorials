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
utils.printfvar('x', x)

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
utils.printfvar(my_func.__name__, my_func)
#
#   execute inner_func
#
my_func()
my_func()
my_func()
