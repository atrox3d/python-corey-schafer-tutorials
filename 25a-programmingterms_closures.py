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

