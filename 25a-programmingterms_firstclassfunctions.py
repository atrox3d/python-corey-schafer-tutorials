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

#################################################################################
utils.banner('high-order functions: pass a function as an argument')


#
#   custom defined map
#
def mymap(func, arglist):
    """
    executes func for every value in arglist
    :returns a list containing the results
    :param func: a function that accepts a value
    :param arglist: a list of values to apply the func to
    """
    utils.printfvar(func.__name__, func)
    utils.printfvar('arglist', arglist)
    result = []
    for i in arglist:
        print(f'applying {func.__name__} to {i}')
        result.append(func(i))
    utils.printfvar('result', result)
    return result


#
#   apply square function to list
#
squares = mymap(square, [1, 2, 3, 4, 5])
utils.printfvar('squares', squares)


def cube(x):
    return square(x) * x


print()
#
#   apply cube function to list
#
cubes = mymap(cube, [1, 2, 3, 4, 5])
utils.printfvar('cubes', cubes)

#################################################################################
utils.banner('first-class functions: return a function from another function')


def logger(msg):
    #
    #   closure: the value of msg will be remembered from by log_message()
    #
    def log_message():
        print(f'Log: {msg}')

    return log_message


#
#   logger initializes log_message with msg = "Hi!"
#
loghi = logger('Hi!')
#
#   loghi() remembers the value of msg when called
#
loghi()


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