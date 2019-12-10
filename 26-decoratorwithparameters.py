#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(f'{prefix} wrapper executed before {original_function.__name__} ({args}, {kwargs})')
            result = original_function(*args, **kwargs)
            print(f'{prefix} wrapper executed after {original_function.__name__} ({args}, {kwargs})')
            return result

        return wrapper_function
    return decorator_function


@prefix_decorator('LOG: ')
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


displayinfo('robb', 49)
