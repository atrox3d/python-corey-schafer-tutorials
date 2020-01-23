"""
https://alex.dzyoba.com/blog/python-import/
"""
# menu.py file

from typing import List

# from pizza import Pizza                   # not working
# from pizzapy.pizza import Pizza           # working version
"""
https://stackoverflow.com/questions/45446418/modulenotfounderror-no-module-named-main-xxxx-main-is-not-a-packag

Note that relative imports are based on the name of the current module. Since the name of the main module is always 
__main__, modules intended for use as the main module of a Python application must always use absolute imports. 
"""
from pizza_app.pizzapy.pizza import Pizza  # most correct version

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
]

if __name__ == '__main__':
    print('menu.py    | ', MENU)
