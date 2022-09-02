#
#   https://www.youtube.com/watch?v=kr0mpwqttM0
#
#   Programming Terms: First-Class Functions
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('function assigning')


def square(x):                                          # returns square of x
    return x * x


utils.printfvar(square, 'square')                       # print function
f = square(5)                                           # assign return value to variable
utils.printfvar(f, 'f')                                 # print f
print()

f = square                                              # assign function to variable
utils.printfvar(f, 'f')                                 # print function f (square)
utils.printfvar(f(5), 'f(5)')                           # print square of 5

#################################################################################
utils.banner('high-order functions: pass a function as an argument')


def mymap(func, arglist):                               # custom defined map
    """
    executes func for every value in arglist
    :returns a list containing the results
    :param func: a function that accepts a value
    :param arglist: a list of values to apply the func to
    """
    utils.printfvar(func, func.__name__)
    utils.printfvar(arglist, 'arglist')
    result = []                                 # initialize return list
    for i in arglist:                           # iterate over argument list
        print(
            f'applying {func.__name__} to {i}'
        )
        result.append(func(i))                  # append result of func
    utils.printfvar(result, 'result')
    return result                               # return list


squares = mymap(square, [1, 2, 3, 4, 5])        # apply square function to list
utils.printfvar(squares, 'squares')


def cube(x):                                    # returns cube of x
    return square(x) * x


print()

cubes = mymap(cube, [1, 2, 3, 4, 5])            # apply cube function to list
utils.printfvar(cubes, 'cubes')

#################################################################################
utils.banner('first-class functions: return a function from another function')


def logger(msg):
    def log_message():                          # closure: the value of msg will be remembered from by log_message()
        print(f'Log: {msg}')                    # points to msg in the stack
    return log_message                          # return inner function


loghi = logger('Hi!')                           # logger initializes log_message with msg = "Hi!"
loghi()                                         # loghi() remembers the value of msg when called


def html(tag):                                  # parametric closure
    print(
        f'creating wrap(): '
        f'<{tag}>{{msg}}</{tag}>'               # points to tag in the stack
    )

    def wrap(msg):                              # will accept msg parameter
        print(f'<{tag}>{msg}</{tag}>')
    return wrap                                 # return inner function


#
#   test our closure
#
h1 = html('H1')
p = html('P')

h1('headline')
p('paragraph')
