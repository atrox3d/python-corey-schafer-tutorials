#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorators normal syntax')


# TODO: implement class decorator

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