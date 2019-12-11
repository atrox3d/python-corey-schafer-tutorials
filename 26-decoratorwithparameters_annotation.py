#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils


def print_innervars(tablevel, prefix=None, original_function=None, *args, **kwargs):
    tabs = "\t" * tablevel
    print(f'{tabs}{"-"*80}')
    print(f'{tabs}print_innervars: prefix            = "{prefix if prefix is not None else "undefined"}"')
    print(f'{tabs}print_innervars: original_function = {original_function if original_function is not None else "UNDEFINED"}')
    print(f'{tabs}print_innervars: args              = {args}')
    print(f'{tabs}print_innervars: kwargs            = {kwargs}')
    print(f'{tabs}{"-"*80}')


def prefixed_decorator(prefix):
    #
    #   1 - set prefix and remeber it into the two inner functions
    #   2 - defines function decorator function and returns it
    #
    print(f'\tprefixed_decorator : called with prefix = "{prefix}"')
    print(f'\tprefixed_decorator : def decorator(original_function)')

    def decorator_function(original_function):
        print(f'\t\tdecorator_function : called with original_function= {original_function}')
        print(f'\t\tdecorator_function : def wrapper_function(*args, **kwargs)')

        def wrapper_function(*args, **kwargs):
            print(f'\t\t\t{prefix} wrapper_function : executed before {original_function.__name__} ({args}, {kwargs})')
            result = original_function(*args, **kwargs)
            print(f'\t\t\t{prefix} wrapper_function : executed after {original_function.__name__} ({args}, {kwargs})')
            print(f'\t\t\twrapper_function : args  : ({args})')
            print(f'\t\t\twrapper_function : kwargs: ({kwargs})')
            print_innervars(3, prefix, original_function, args, kwargs)
            print()
            return result

        print_innervars(2, prefix=prefix, original_function=original_function)
        print('\t\tdecorator_function : return wrapper_function')
        print()
        return wrapper_function

    print_innervars(1, prefix=prefix)
    print(f'\tprefixed_decorator : return decorator_function = {decorator_function}')
    print()
    return decorator_function


print("main : @prefixed_decorator('LOG: ')")


# same as:
# prefixed_dec = prefixed_decorator('LOG: ')
# prefixed_display = prefixed_dec(displayinfo)
# prefixed_display('john', 30)


@prefixed_decorator('LOG: ')
def displayinfo(name, age):
    print(f'displayinfo : displayinfo ran with arguments ({name}, {age})')


print("main : execute displayinfo('robb', 49)")
displayinfo('robb', 49)
