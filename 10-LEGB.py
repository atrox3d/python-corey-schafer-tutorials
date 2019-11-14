#
# https://www.youtube.com/watch?v=QVdf0LgmICw
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
    printx(x, 'enclosingx')

    def enclosedx():
        # comment or decomment to change x scope
        # x = 'enclosed x'
        printx(x, 'enclosedx')

    enclosedx()


globalx()
localx()
enclosingx()
printx(x)
