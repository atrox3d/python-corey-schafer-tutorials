#
#   https://www.youtube.com/watch?v=x3v9zMX1s4s
#
#################################################################################
from modules import utils
from modules.duck import Duck
from modules.person import Person

#################################################################################
#
#
#   ducktyping (non pythonic)
#   LBYL: look before you leap
#
#
#################################################################################

utils.banner('ducktyping | non pythonic | LBYL: look before you leap')


def quackandfly_ifclass(thing):
    # LBYL
    # non pythonic
    # not duck-typed
    if isinstance(thing, Duck):
        print(f'ok, this is a {thing.__class__.__name__}')
        thing.quack()
        thing.fly()
    else:
        print(f'this is no duck, this is a {thing.__class__.__name__}')
    print()


def quackandfly_ifmethod(thing):
    # LBYL
    # non pythonic
    # not duck-typed
    if hasattr(thing, 'quack'):
        if callable(thing.quack):
            thing.quack()

    if hasattr(thing, 'fly'):
        if callable(thing.fly):
            thing.fly()
    print()


duck = Duck()
person = Person()

quackandfly_ifclass(duck)
quackandfly_ifclass(person)

quackandfly_ifmethod(duck)
quackandfly_ifmethod(person)
