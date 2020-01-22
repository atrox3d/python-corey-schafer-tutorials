"""
https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
"""
from pizza_app.pizzapy import menu
from pizza_app.pizzapy import pizza

print(menu.MENU)
mypizza = pizza.Pizza('profumata', 30, 12)
print(mypizza)


class Pizza(pizza.Pizza):
    def __str__(self):
        return f'{self.name}({self.size}): EUR {self.price}'


oldpizza = pizza.Pizza('oldpizza', 0, 0)
newpizza = Pizza('strpizza', 0, 0)
print(oldpizza)
print(newpizza)
