#
#   https://www.youtube.com/watch?v=x3v9zMX1s4s
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
    for x in range(1, n):
        yield x


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