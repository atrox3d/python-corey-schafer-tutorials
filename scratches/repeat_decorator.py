import functools


def repeat(num_times):
    """
    sets num_times in the closure

    defines decorator_repeat(func)

    :return: decorator_repeat
    """

    def decorator_repeat(func):
        """
        defines wrapper_repeat(*args, **kwargs)

        :returns: wrapper_repeat
        """

        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            """
            func(*args, **kwargs) num_times

            :return:    last return value
            """
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat


@repeat(4)
def hello():
    print('hello')


def hello2():
    print('hello2')


def hello3():
    print('hello3')


hello()
print()

hello2 = repeat(2)(hello2)
hello2()
print()

repeater = repeat(3)
repeated = repeater(hello3)

repeated()
print()
