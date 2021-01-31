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
def get_simplegenerator(n=10):
    print('-----------------------------------------------------------------------')
    print('entering generator loop')
    print('-----------------------------------------------------------------------')
    for x in range(1, n):
        print(f'{"yielding":>20} | x={x}')
        yield x
        print(f'{"after single yield":>20} | x={x}')
    print(f'{"after yield block":>20} | x={x}')
    print('-----------------------------------------------------------------------')
    print('exiting generator loop')
    print('-----------------------------------------------------------------------')


gen = get_simplegenerator()

utils.banner('generator functions')
utils.printfvar(gen, 'gen')
for g in gen:
    utils.printfvar(g, 'g')

gen = list(get_simplegenerator())

utils.banner('generator functions as list')
utils.printfvar(gen, 'gen')
for g in gen:
    utils.printfvar(g, 'g')
########################################################################################################################
#def subgen