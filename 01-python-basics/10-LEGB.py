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


def printx(x, context='global'):                    # shadows global x with local
    print(f'{context} - x: {x}')


def globalx():                                      # uses global x
    printx(x, 'function globalx')


def localx():                                       # passes global or local x
    # x = 'local x'                                   # comment or decomment to change x scope
    printx(x, 'function localx')


def enclosingx():                                   # test nonlocal keyword with nested function
    """
    What is nonlocal keyword in Python

    The nonlocal keyword won’t work on local or
    global variables and therefore must be used to
    reference variables in another scope except
    the global and local one.

    The nonlocal keyword is used in nested functions
    to reference a variable in the parent function.
    :return:
    """
    # x = 'enclosing x'                               # comment or decomment to change x scope
    printx(x, 'function enclosingx')

    def enclosedx():                                # nested function
        # nonlocal x                                  # decomment only if x is defined in enclosingx()
        # x = 'enclosed x'                            # comment or decomment to change x scope
        printx(x, 'function enclosedx')

    enclosedx()
    printx(x, 'function enclosingx')


globalx()
localx()
enclosingx()
printx(x)
