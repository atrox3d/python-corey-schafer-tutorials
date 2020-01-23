"""
https://alex.dzyoba.com/blog/python-import/
https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
"""


def filternames(collection, *exclude):
    """
    print collection, excluding dunders and names in the optional list
    :param collection:
    :param exclude:
    :return:
    """
    exclude = list(exclude)
    exclude.append(filternames.__name__)
    if type(collection) is list:
        return [name for name in collection if not name.startswith('_') and name not in exclude]
    elif type(collection) is dict:
        return {key: val for key, val in collection.items() if not key.startswith('_') and key not in exclude}
    else:
        raise TypeError('need list or dicct')


def print_prettifycollection(name, collection, indent=4):
    print(f'{name}:')
    if type(collection) is list:
        for name in collection:
            print(' ' * indent, name)
    elif type(collection) is dict:
        for key, val in collection.items():
            print(' ' * indent, f'{key:<10}: {val}')


def printnames():
    print('-----------------------------------------------------------------------------------------------------------')
    _locals = filternames(locals(), printnames.__name__, print_prettifycollection.__name__)
    _globals = filternames(globals(), printnames.__name__, print_prettifycollection.__name__)
    _dir = filternames(dir(), printnames.__name__, print_prettifycollection.__name__)

    if _locals:
        print_prettifycollection('locals : ', _locals)

    if _globals:
        print_prettifycollection('globals: ', _globals)

    if _dir:
        print_prettifycollection('dir    : ', _dir)

    if not _locals and not _globals and not _dir:
        print("NO VALUES in locals, globals and dir")
    print('############################################################################################################')


printnames()
#
#
#
print('import pizza_app:')
import pizza_app                                    # creates namespace pizza_app
print(pizza_app)
# print(pizza_app.pizzapy)                          # AttributeError: module 'pizza_app' has no attribute 'pizzapy'
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app' has no attribute 'pizzapy'
printnames()
#
#
#
print('import pizza_app.pizzapy:')
import pizza_app.pizzapy
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app.pizzapy' has no attribute 'pizza'
print(pizza_app.pizzapy)
printnames()
#
#
#
print('from pizza_app import pizzapy:')
from pizza_app import pizzapy                       # creates namespace pizzapy
print(pizza_app.pizzapy)
print(pizzapy)
# pizzapy.pizza.Pizza('', 0, 0)                     # NO
printnames()
#
#
#
print('import pizza_app.pizzapy.pizza:')
import pizza_app.pizzapy.pizza                      #
# Pizza('name', 10, 10.0)                           # NameError: name 'Pizza' is not defined
print(pizza_app.pizzapy.pizza)
# print(pizza)                                      # NameError: name 'pizza' is not defined
printnames()
pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)     # YES
#
#
#
print('from pizza_app.pizzapy import pizza:')
from pizza_app.pizzapy import pizza                 # creates namespace pizza
# Pizza('name', 10, 10.0)                           # NameError: name 'Pizza' is not defined
print(pizza_app.pizzapy.pizza)
print(pizza)
printnames()
pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)     # YES
#
#
#
# import pizza_app.pizzapy.pizza.Pizza              # ModuleNotFoundError: No module named 'pizza_app.pizzapy.pizza.Pizza'; 'pizza_app.pizzapy.pizza' is not a package
#
#
#
print('from pizza_app.pizzapy.pizza import Pizza:')
from pizza_app.pizzapy.pizza import Pizza           # creates class Pizza in namespace
print(pizza_app.pizzapy.pizza)
print(pizza)
print(Pizza)
printnames()
Pizza('name', 10, 10.0)                             # YES
print()
print()
print()
print()
print()
print('RESET imports')
print()
print()
print()
print()
print()
#
#
#
print('del pizza_app.pizzapy.pizza.Pizza:')
del pizza_app.pizzapy.pizza.Pizza                   # no effect
printnames()
#
#
#
print('del Pizza:')
del Pizza                                           # deletes Pizza
printnames()
#
#
#
print('del pizza_app.pizzapy.pizza:')
del pizza_app.pizzapy.pizza                         # no effect
printnames()
#
#
#
print('del pizza:')
del pizza                                           # removes namespace pizza
printnames()
#
#
#
print('del pizza_app.pizzapy:')
del pizza_app.pizzapy                               # no effect
printnames()
#
#
#
print('del pizzapy:')
del pizzapy                                         # removes namespace pizzapy
printnames()
#
#
#
print('del pizza_app:')
del pizza_app                                       # removes namespace pizza
printnames()
















