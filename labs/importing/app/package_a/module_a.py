"""
https://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
"""
import app.package_b.module_b
from os import path

# myself: str = __file__.split('/').pop()
myself = path.basename(__file__)

print(f'{myself:<15}| as {__name__}')
