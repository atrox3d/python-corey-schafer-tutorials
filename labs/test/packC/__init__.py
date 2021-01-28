"""
https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html
"""
import os
import os.path

thisfile = os.path.relpath(__file__, '..')

print(f'{thisfile:<25} | from . import c1')
# this import makes c1_func directly accessible from packC.c1.c1_func
from . import c1


## this import makes c1_func directly accessible from packC.c1_func
from packC.c1 import c1_func


