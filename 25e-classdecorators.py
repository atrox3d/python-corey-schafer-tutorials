#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorators normal syntax')


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f'call method executed this before {self.original_function.__name__}')
        return self.original_function(*args, **kwargs)


def display():
    print('display function ran')


decorated_display = DecoratorClass(display)
decorated_display()


#################################################################################
utils.banner('decorators annotated syntax')


#
#   this is the same as:
#           decorated_display = decorator_function(display)
@DecoratorClass
def display():
    print('display function ran')


@DecoratorClass
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


display()
displayinfo('john', 25)
