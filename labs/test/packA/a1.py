"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')
print(f'{thisfile:<25} | ')


def a1_func():
    print(f'{thisfile:<25} | running packA.a1.a1_func()')

