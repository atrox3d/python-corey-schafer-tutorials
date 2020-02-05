"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')
#
#   packA
#
print(f'{thisfile:<25} | import packA')
import packA  # "import packA.a1" will work just the same
print(f'{thisfile:<25} | packA imported\n')
#
#   functions
#
print(f'{thisfile:<25} | call | packA.packA_func()')
packA.packA_func()
print(f'{thisfile:<25} | call | packA.a1_func()')
packA.a1_func()
print(f'{thisfile:<25} | call | packA.a1.a1_func()')
packA.a1.a1_func()
#
#   packA.subA : solution 1
#
print(f'{thisfile:<25} | from packA.subA.sa1 import helloWorld')
from packA.subA.sa1 import helloWorld
print(f'{thisfile:<25} | call | helloWorld()')
helloWorld()
#
#   packA.subA : solution 2
#
print(f'{thisfile:<25} | from packA.subA import sa1')
from packA.subA import sa1
print(f'{thisfile:<25} | call | sa1.helloWorld()')
sa1.helloWorld()
#
#   packA.subA : solution 3
#
print(f'{thisfile:<25} | import packA.subA.sa1')
import packA.subA.sa1
print(f'{thisfile:<25} | call | packA.subA.sa1.helloWorld()')
packA.subA.sa1.helloWorld()
