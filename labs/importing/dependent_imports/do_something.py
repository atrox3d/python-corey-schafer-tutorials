"""
append parent dir to enable import manually
"""
import sys
print('appending .. to sys.path')
sys.path.append('..')

"""
import symbol
"""
if __name__ == '__main__':
    from dependent_imports.config import INDENT_WIDTH
else:
    from .config import INDENT_WIDTH

print(" " * INDENT_WIDTH, "hello")