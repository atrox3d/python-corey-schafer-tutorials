"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')
print(f'{thisfile:<25} | ')


def helloWorld():
    print(f'{thisfile:<25} | running packA.subA.sa1.helloWorld()')
