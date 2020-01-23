import pizza_app                                    # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # NO

import pizza_app.pizzapy                            # useless
# pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)   # NO

import pizza_app.pizzapy.pizza                      #
# Pizza('name', 10, 10.0)                           # NO
pizza_app.pizzapy.pizza.Pizza('name', 10, 10.0)     # YES

# import pizza_app.pizzapy.pizza.Pizza              # NO
from pizza_app.pizzapy.pizza import Pizza           # YES
Pizza('name', 10, 10.0)                             # YES









