"""
https://alex.dzyoba.com/blog/python-import/
"""
"""
https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag
"""
# menu.py file

from typing import List
# from pizza import Pizza                   # not working
# from pizzapy.pizza import Pizza           # working version
from pizza_app.pizzapy.pizza import Pizza   # most correct version

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
]

if __name__ == '__main__':
    print('menu.py    | ', MENU)

