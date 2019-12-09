#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils


utils.banner('decorators')


def decorator_function(original_function):
    def wrapper_function():
        return original_function()

    return wrapper_function


def display():
    print('display function ran')


decorated_display = decorator_function(display)
decorated_display()
