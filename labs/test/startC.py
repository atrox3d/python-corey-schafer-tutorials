"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')
#
#   packA
#
print(f'{thisfile:<25} | import packC')
import packC  # "import packA.a1" will work just the same
print(f'{thisfile:<25} | packC imported\n')
print(f'{thisfile:<25} | {packC}\n')

packC.c1.c1_func()
packC.c1_func()

