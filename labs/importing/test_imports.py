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


def printnames():
    print('-----------------------------------------------------------------------------------------------------------')
    _locals = filternames(locals(), printnames.__name__)
    _globals = filternames(globals(), printnames.__name__)
    _dir = filternames(dir(), printnames.__name__)

    if _locals:
        print('locals : ', _locals)

    if _globals:
        print('globals: ', _globals)

    if _dir:
        print('dir    : ', _dir)

    if not _locals and not _globals and not _dir:
        print("NO VALUES in locals, globals and dir")
    print('############################################################################################################')


printnames()

print('import pizza_app:')
import pizza_app                                    # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app' has no attribute 'pizzapy'
printnames()
#
#
#
print('import pizza_app.pizzapy:')
import pizza_app.pizzapy                            # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app.pizzapy' has no attribute 'pizza'
printnames()
#
#
#
print('from pizza_app import pizzapy:')
from pizza_app import pizzapy
# pizzapy.pizza.Pizza('', 0, 0)                     # NO
printnames()
#
#
#
print('import pizza_app.pizzapy.pizza:')
import pizza_app.pizzapy.pizza                      #
# Pizza('name', 10, 10.0)                           # NameError: name 'Pizza' is not defined
printnames()
pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)     # YES
#
#
#
# import pizza_app.pizzapy.pizza.Pizza              # ModuleNotFoundError: No module named 'pizza_app.pizzapy.pizza.Pizza'; 'pizza_app.pizzapy.pizza' is not a package
print('from pizza_app.pizzapy.pizza import Pizza:')
from pizza_app.pizzapy.pizza import Pizza           # YES
printnames()
Pizza('name', 10, 10.0)                             # YES
"""
RESET imports
"""
#
#
#
print('del Pizza:')
del Pizza
printnames()
#
#
#
print('del pizza_app.pizzapy.pizza.Pizza:')
del pizza_app.pizzapy.pizza.Pizza
printnames()
#
#
#
print('del pizza_app.pizzapy.pizza:')
del pizza_app.pizzapy.pizza
printnames()
#
#
#
print('del pizza_app.pizzapy:')
del pizza_app.pizzapy
printnames()
#
#
#
print('del pizzapy:')
del pizzapy
printnames()
#
#
#
print('del pizza_app:')
del pizza_app
printnames()
















