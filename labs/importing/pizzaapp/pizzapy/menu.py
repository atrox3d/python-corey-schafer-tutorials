"""
https://alex.dzyoba.com/blog/python-import/
"""
# menu.py file

from typing import List

if __name__ == '__main__':
    """
    if __name__ == '__main__' then the dot becomes:
        from __main__.pizza
    
    so, to avoid the error we test __name__ and omit the dot
    """
    from pizza import Pizza
else:
    from .pizza import Pizza

MENU: List[Pizza] = [
    Pizza('Margherita', 30, 10.0),
    Pizza('Carbonara', 45, 14.99),
    Pizza('Marinara', 35, 16.99),
]

if __name__ == '__main__':
    print(MENU)
