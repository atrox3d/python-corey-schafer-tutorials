def filternames(collection, exclude=[]):
    """
    print collection, excluding dunders and names in the optional list
    :param collection:
    :param exclude:
    :return:
    """
    exclude.append(filternames.__name__)
    if type(collection) is list:
        return [name for name in collection if not name.startswith('__') and name not in exclude]
    elif type(collection) is dict:
        return {key: val for key, val in collection.items() if not key.startswith('__') and key not in exclude}
    else:
        raise TypeError('need list or dicct')


def printnames():
    print('############################################################################################################')
    print('locals : ', filternames(locals(), [printnames.__name__]))
    print('globals: ', filternames(globals(), [printnames.__name__]))
    print('dir    : ', filternames(dir(), [printnames.__name__]))
    print('############################################################################################################')


printnames()

print('import pizza_app:')
import pizza_app                                    # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app' has no attribute 'pizzapy'
printnames()

print('import pizza_app.pizzapy')
import pizza_app.pizzapy                            # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # AttributeError: module 'pizza_app.pizzapy' has no attribute 'pizza'
printnames()

print('import pizza_app.pizzapy.pizza')
import pizza_app.pizzapy.pizza                      #
# Pizza('name', 10, 10.0)                           # NameError: name 'Pizza' is not defined
printnames()
pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)     # YES

# import pizza_app.pizzapy.pizza.Pizza              # ModuleNotFoundError: No module named 'pizza_app.pizzapy.pizza.Pizza'; 'pizza_app.pizzapy.pizza' is not a package
print('from pizza_app.pizzapy.pizza import Pizza')
from pizza_app.pizzapy.pizza import Pizza           # YES
printnames()
Pizza('name', 10, 10.0)                             # YES
"""
RESET imports
"""
# del Pizza
# del pizza_app.pizzapy.pizza.Pizza
# del pizza_app.pizzapy.pizza
# del pizza_app.pizzapy
# del pizza_app

# print('locals : ', locals())
# print('globals: ', globals())
# print('dir    : ', dir())
# from pizza_app.pizzapy.pizza import Pizza
# print('locals : ', locals())
# print('globals: ', globals())
# print('dir    : ', dir())










