from modules import utils
import functools

########################################################################################################################
utils.banner(
    'https://realpython.com/primer-on-python-decorators/#debugging-code',
    'debugging decorator'
)


def debug_decorator(func):
    """Print the function signature and value"""

    debug = False

    @functools.wraps(func)
    def debug_wrapper(*args, **kwargs):

        """create list of repr of each arg"""
        args_repr = [repr(a) for a in args]  # 1
        if debug: print('args_repr =', args_repr)

        """create list of repr of each kwarg"""
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]  # 2
        if debug: print('kwargs_repr =', kwargs_repr)

        """create signature"""
        signature = ", ".join(args_repr + kwargs_repr)
        if debug: print(args_repr + kwargs_repr)
        if debug: print(signature)

        print(f'calling {func.__name__}({signature!r})')
        value = func(*args, **kwargs)
        print(f'{func.__name__!r} returned {value!r}')

        return value

    return debug_wrapper


@debug_decorator
def hello(*args, **kwargs):
    print('hello')
    return 0


hello(1, "2", '3', kwargs1=1, name='robb')


