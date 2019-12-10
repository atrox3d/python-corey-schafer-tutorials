#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils


def prefixed_decorator(prefix):
    print(f'\tprefixed_decorator : called with prefix = "{prefix}"')
    print(f'\tprefixed_decorator : def decorator(original_function)')

    def decorator_function(original_function):
        print(f'\t\tdecorator_function : called with original_function= {original_function}')
        print(f'\t\tdecorator_function : def wrapper_function(*args, **kwargs)')

        def wrapper_function(*args, **kwargs):
            print(f'\t\t\t{prefix} wrapper_function : executed before {original_function.__name__} ({args}, {kwargs})')
            result = original_function(*args, **kwargs)
            print(f'\t\t\t{prefix} wrapper_function : executed after {original_function.__name__} ({args}, {kwargs})')
            return result

        print('\t\tdecorator_function : return wrapper_function')
        return wrapper_function

    print('\tprefixed_decorator : return decorator_function')
    return decorator_function


print("main : @prefixed_decorator('LOG: ')")


@prefixed_decorator('LOG: ')
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


print("main : execute displayinfo('robb', 49)")
displayinfo('robb', 49)


