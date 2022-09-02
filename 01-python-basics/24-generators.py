#
#   https://www.youtube.com/watch?v=bD05uGo_sVI
#
#   Python Tutorial: Generators - How to use them and the benefits you receive
#
#################################################################################
from modules import utils


#################################################################################
#
#
#   generator functions
#
#
#################################################################################


def get_simplegenerator(n=10, maxlen=utils.MAXLEN):                             # define function with param
    print('----------------------------------------')
    print('entering generator loop')
    print('----------------------------------------')
    # maxlen = 30
    for x in range(1, n):                                                       # loop from 1 to n-1
        print(f'{"generator: yielding":>{maxlen}.{maxlen}} | x={x}')            # print yielding value
        yield x                                                                 # returns x and waits for the next iteration
        print(f'{"generator: after single yield":>{maxlen}.{maxlen}} | x={x}')  # executed after outer loop block
        print("-------------")
    print(f'{"generator: after yield loop":>{maxlen}.{maxlen}} | x={x}')       # executed after inner for loop

    print('-----------------------------------------------------------------------')
    print('exiting generator loop')
    print('-----------------------------------------------------------------------')


gen = get_simplegenerator()

utils.banner('generator functions')
utils.printfvar(gen, 'gen')
for g in gen:
    print(f'{"main loop: iterating":>{utils.MAXLEN}.{utils.MAXLEN}} | g={g}')  # print yielding value
    utils.printfvar(g)
    print(f'{"main loop: end of loop block":>{utils.MAXLEN}.{utils.MAXLEN}} | g={g}')  # print yielding value

gen = list(get_simplegenerator())

utils.banner('generator functions as list')
utils.printfvar(gen, 'gen')
for g in gen:
    utils.printfvar(g, 'g')
################################################################################
#def subgen