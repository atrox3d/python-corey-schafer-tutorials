#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#   Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorators normal syntax')


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed before {original_function.__name__} ({args}, {kwargs})')
        return original_function(*args, **kwargs)

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


@decorator_function
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


display()
displayinfo('john', 25)