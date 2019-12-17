import functools


def stateful_decorator(func):
    """
    defines stateful_wrapper(*args, **kwargs)

    returns statefulwrapper
    """
    stateful_decorator.count = stateful_decorator.count + 1 if hasattr(stateful_decorator, 'count') else 0
    print(f'decorator usage: {stateful_decorator.count}')

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
        print(f'wrapper function: {stateful_wrapper.wrapperfunc}')
        print(f'wrapped function: {stateful_wrapper.wrappedfunc}')
        value = func(*args, **kwargs)
        return value

    return stateful_wrapper


@stateful_decorator
def hello(name='bob'):
    print(f'hello {name}')


@stateful_decorator
def hello(name='bob'):
    print(f'hello {name}')


hello()
print(hello.wrapperfunc)
print(hello.wrappedfunc)
