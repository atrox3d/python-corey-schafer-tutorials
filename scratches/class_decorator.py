import functools
from modules import utils

########################################################################################################################
utils.banner(
    'https://realpython.com/primer-on-python-decorators/#classes-as-decorators',
    'class as decorator'
)


class CountCalls:
    def __init__(self, func):
        """
        The .__init__() method must store a reference to the function and can do any other necessary initialization.

        Note that you need to use the functools.update_wrapper() function instead of @functools.wraps.

        :param func:
        """
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        """
        The .__call__() method will be called instead of the decorated function. It does essentially the same thing as the wrapper() function in our earlier examples.

        :param args:
        :param kwargs:
        :return: func(*args, **kwargs)
        """
        self.num_calls += 1
        print(f'call {self.num_calls} of {self.func.__name__!r}')
        return self.func(*args, **kwargs)


@CountCalls
def say_whee():
    print('whee')


say_whee()
say_whee()
say_whee()
