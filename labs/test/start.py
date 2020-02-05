"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')

print(f'{thisfile:<25} | import packA')
import packA  # "import packA.a1" will work just the same
print(f'{thisfile:<25} | packA imported\n')

print(f'{thisfile:<25} | call | packA.packA_func()')
packA.packA_func()
print(f'{thisfile:<25} | call | packA.a1_func()')
packA.a1_func()
print(f'{thisfile:<25} | call | packA.a1.a1_func()')
packA.a1.a1_func()
