"""
https://alex.dzyoba.com/blog/python-import/
"""
# menu.py file

from typing import List
# from pizza import Pizza
from pizzapy.pizza import Pizza

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
]

if __name__ == '__main__':
    print(MENU)

