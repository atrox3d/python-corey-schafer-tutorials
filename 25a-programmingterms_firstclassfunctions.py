#
#   https://www.youtube.com/watch?v=kr0mpwqttM
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('function assigning')


def square(x):
    return x * x


utils.printfvar('square', square)
#
# assign return value to variable
#
f = square(5)
utils.printfvar('f', f)

print()
#
# assign function to variable
#
f = square
utils.printfvar('f', f)
utils.printfvar('f(5)', f(5))

