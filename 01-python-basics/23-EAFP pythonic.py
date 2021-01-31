#
#   https://www.youtube.com/watch?v=x3v9zMX1s4s
#
#   Python Tutorial: Duck Typing and Asking Forgiveness, Not Permission (EAFP)
#
#################################################################################
from modules import utils
from modules.duck import Duck
from modules.person import Person

#################################################################################
#
#
#   ducktyping (pythonic)
#   EAFP: easier ask forgiveness than permission
#
#
#################################################################################
utils.banner('ducktyping | pythonic | EAFP: easier ask forgiveness than permission')


def quackandfly(thing):
    # EAFP
    # pythonic
    # duck-typed
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as ae:
        print(ae)

    print()


duck = Duck()
quackandfly(duck)

person = Person()
quackandfly(person)
