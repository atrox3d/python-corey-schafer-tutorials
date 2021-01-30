#
# https://www.youtube.com/watch?v=QVdf0LgmICw
#
# Python Tutorial: Variable Scope - Understanding the LEGB rule and global/nonlocal statements
#
#################################################################################
"""
LEGB
local, enclosing, global, builtin
"""

x = 'global x'


def printx(x, context='global'):
    print(f'{context} - x: {x}')


def globalx():
    printx(x, 'function globalx')


def localx():
    # comment or decomment to change x scope
    # x = 'local x'
    printx(x, 'function localx')


def enclosingx():
    # comment or decomment to change x scope
    # x = 'enclosing x'
    printx(x, 'function enclosingx')

    def enclosedx():
        # decomment only if x is defined in enclosingx()
        # nonlocal x
        # comment or decomment to change x scope
        # x = 'enclosed x'
        printx(x, 'function enclosedx')

    enclosedx()
    printx(x, 'function enclosingx')


globalx()
localx()
enclosingx()
printx(x)
