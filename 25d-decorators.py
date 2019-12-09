#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorators normal syntax')


def decorator_function(original_function):
    def wrapper_function():
        print(f'wrapper executed before {original_function.__name__}')
        return original_function()

    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()

#################################################################################
utils.banner('decorators annotated syntax')


#
#   this is the same as:
#           decorated_display = decorator_function(display)
@decorator_function
def display():
    print('display function ran')


display()

