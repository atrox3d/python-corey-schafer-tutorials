#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils


def print_innervars(tablevel, prefix=None, original_function=None, *args, **kwargs):
    tabs = "\t" * tablevel
    print(f'{tabs}{"-" * 80}')
    print(f'{tabs}print_innervars: prefix            = "{prefix if prefix is not None else "undefined"}"')
    print(
        f'{tabs}print_innervars: original_function = {original_function if original_function is not None else "UNDEFINED"}')
    print(f'{tabs}print_innervars: args              = {args}')
    print(f'{tabs}print_innervars: kwargs            = {kwargs}')
    print(f'{tabs}{"-" * 80}')


def prefixed_decorator(prefix):
    #
    #   1 - set prefix and remeber it into the two inner functions
    #   2 - defines function decorator function and returns it
    #
    print(f'\tprefixed_decorator : called with prefix = "{prefix}"')
    print(f'\tprefixed_decorator : def decorator(original_function)')

    #
    #   define decorator_function
    #
    def decorator_function(original_function):
        print(f'\t\tdecorator_function : called with original_function= {original_function}')
        print(f'\t\tdecorator_function : def wrapper_function(*args, **kwargs)')

        #
        #   define wrapper_function
        #
        def wrapper_function(*args, **kwargs):
            print(f'\t\t\t{prefix} wrapper_function : executed before {original_function.__name__} ({args}, {kwargs})')
            result = original_function(*args, **kwargs)
            print(f'\t\t\t{prefix} wrapper_function : executed after {original_function.__name__} ({args}, {kwargs})')
            print(f'\t\t\twrapper_function : args  : ({args})')
            print(f'\t\t\twrapper_function : kwargs: ({kwargs})')
            print_innervars(3, prefix, original_function, args, kwargs)
            print()
            #
            #   return original_function value
            #
            return result

        print_innervars(2, prefix=prefix, original_function=original_function)
        print('\t\tdecorator_function : return wrapper_function')
        print()
        #
        #   return pointer to wrapper_function
        #
        return wrapper_function

    print_innervars(1, prefix=prefix)
    print(f'\tprefixed_decorator : return decorator_function = {decorator_function}')
    print()
    #
    #   return pointer to decorator_function
    #
    return decorator_function


print('main : define display_info')


def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


# works
print(f"main : prefixed_dec = prefixed_decorator('LOG: ')")
prefixed_dec = prefixed_decorator('LOG: ')
print()
print(f'main : prefixed_dec = {prefixed_dec}')
print(f'main : prefixed_dec name = {prefixed_dec.__name__}')
print(f"main : prefixed_display = prefixed_dec(displayinfo)")
prefixed_display = prefixed_dec(displayinfo)
print()
print(f'main : prefixed_display = {prefixed_display}')
print(f'main : prefixed_display name = {prefixed_display.__name__}')

print("main : prefixed_display('john', 30)")
prefixed_display('john', 30)
