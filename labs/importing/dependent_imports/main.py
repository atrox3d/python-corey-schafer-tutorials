"""
append parent dir to enable import manually
"""
import sys
sys.path.append('..')

"""
import symbol which is in turn, imported by do_something.py
"""
from dependent_imports.do_something import INDENT_WIDTH


print(INDENT_WIDTH)
from dependent_imports import do_something


