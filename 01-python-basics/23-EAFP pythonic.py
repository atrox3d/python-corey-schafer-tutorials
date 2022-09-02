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
#
#    LBYL: Look Before You Leap (non pythonic)
#
#################################################################################
utils.banner('ducktyping | pythonic | EAFP: easier ask forgiveness than permission')


def quackandfly(thing):                                 # EAFP
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as ae:                        # ask forgiveness
        print(ae)
    print()


def lbyl(thing):                                        # LBYL
    if hasattr(thing, 'quack'):                         # ask for permission
        if callable(thing.quack):                       # ask for permission
            thing.quack()


duck = Duck()
quackandfly(duck)

person = Person()
quackandfly(person)
