"""
https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
"""
import pizza_app_experiments.pizzapy.menu               # need to use FQN: pizza_app_experiments.pizzapy.menu.MENU
print(pizza_app_experiments.pizzapy.menu.MENU)

from pizza_app_experiments.pizzapy import menu          # need to use just menu.MENU
print(menu.MENU)

"""
this doesnt work, you cannot import a class directly
"""
# import pizza_app_experiments.pizzapy.pizza.Pizza
# mypizza = pizza_app_experiments.pizzapy.pizza.Pizza('pizza.Pizza', 30, 12)
# print(mypizza)

from pizza_app_experiments.pizzapy import pizza         # need to use pizza.Pizza
mypizza = pizza.Pizza('pizza.Pizza', 30, 12)
print(mypizza)

from pizza_app_experiments.pizzapy.pizza import Pizza   # need to use just Pizza
mypizza = Pizza('just Pizza', 30, 12)
print(mypizza)


class Pizza(pizza.Pizza):
    def __str__(self):
        return f'{self.name}({self.size}): EUR {self.price}'


oldpizza = pizza.Pizza('oldpizza', 0, 0)
newpizza = Pizza('strpizza', 0, 0)
print(oldpizza)
print(newpizza)
