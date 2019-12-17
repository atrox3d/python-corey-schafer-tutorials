import functools
from modules import utils

########################################################################################################################
utils.banner(
    'https://realpython.com/primer-on-python-decorators/#stateful-decorators',
    'stateful decorator'
)


def stateful_decorator(func):
    """
    defines stateful_wrapper(*args, **kwargs)

    returns statefulwrapper
    """

    #
    #   setup counter hattribute
    #
    stateful_decorator.counter = stateful_decorator.counter + 1 if hasattr(stateful_decorator, 'counter') else 0
    print(f'stateful_decorator | decorator usage: {stateful_decorator.counter}')

    @functools.wraps(func)
    def stateful_wrapper(*args, **kwargs):
        """
        saves function attributes:
            - .wrapperfunc
            - .wrappedfunc
        """
        # stateful_wrapper.wrapperfunc = stateful_wrapper.__name__
        stateful_wrapper.wrapperfunc = "stateful_wrapper"
        stateful_wrapper.wrappedfunc = func.__name__
        print(f'stateful_wrapper   | wrapper function : {stateful_wrapper.wrapperfunc}')
        print(f'stateful_wrapper   | wrapped function : {stateful_wrapper.wrappedfunc}')
        print(f'stateful_wrapper   | decorator usage  : {stateful_decorator.counter}')
        value = func(*args, **kwargs)
        return value

    return stateful_wrapper


@stateful_decorator
def hello(name='bob'):
    print(f'hello {name}')


@stateful_decorator
def hello(name='bob'):
    print(f'hello {name}')


@stateful_decorator
def hellox(name='bob'):
    print(f'hello {name}')


hello()
print(hello.wrapperfunc)
print(hello.wrappedfunc)
