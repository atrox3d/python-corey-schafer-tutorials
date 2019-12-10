#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorator practical examples')


def mylogger(func):
    import logging
    import os
    #
    #   create logfile path and configure logger
    #
    filename = os.path.join(os.getcwd(), 'data', f'{func.__name__}.log')
    logging.basicConfig(filename=filename, level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'ran with args: {} and kwargs: {}'.format(args, kwargs)
        )
        return func(*args, **kwargs)

    return wrapper


