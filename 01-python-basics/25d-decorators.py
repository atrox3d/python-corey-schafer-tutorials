#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#   Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorators normal syntax')


def decorator_function(original_function):              # define decorator func takes function as param
    def wrapper_function(*args, **kwargs):              # define weapper func will accept any param
        print(                                          # will be executed in place of original_functions
            f'wrapper executed before '
            f'{original_function.__name__} '
            f'({args}, {kwargs})'
        )
        return original_function(*args, **kwargs)       # will execute original_function and return its return value

    return wrapper_function                             # returns the wrapped function


def display():
    print('display function ran')


decorated_display = decorator_function(display)         # assigning wrapper_function
decorated_display()

#################################################################################
utils.banner('decorators annotated syntax')


@decorator_function                                     # this is the same as: display = decorator_function(display)
def display():
    print('display function ran')


@decorator_function                                     # this is the same as: displayinfo = decorator_function(displayinfo)
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


display()
displayinfo('john', 25)