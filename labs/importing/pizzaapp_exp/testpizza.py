"""
https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
"""
import pizzaapp_exp.pizzapy.menu               # need to use FQN: pizzaapp_exp.pizzapy.menu.MENU
print(pizzaapp_exp.pizzapy.menu.MENU)

from pizzaapp_exp.pizzapy import menu          # need to use just menu.MENU
print(menu.MENU)

"""
this doesnt work, you cannot import a class directly
"""
# import pizzaapp_exp.pizzapy.pizza.Pizza
# mypizza = pizzaapp_exp.pizzapy.pizza.Pizza('pizza.Pizza', 30, 12)
# print(mypizza)

from pizzaapp_exp.pizzapy import pizza         # need to use pizza.Pizza
mypizza = pizza.Pizza('pizza.Pizza', 30, 12)
print(mypizza)

from pizzaapp_exp.pizzapy.pizza import Pizza   # need to use just Pizza
mypizza = Pizza('just Pizza', 30, 12)
print(mypizza)


class Pizza(pizza.Pizza):
    def __str__(self):
        return f'{self.name}({self.size}): EUR {self.price}'


oldpizza = pizza.Pizza('oldpizza', 0, 0)
newpizza = Pizza('strpizza', 0, 0)
print(oldpizza)
print(newpizza)
