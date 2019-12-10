#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils

#################################################################################
utils.banner('decorator practical examples: logger')


def mylogger(func):
    import logging
    import os
    #
    #   create logfile path and configure logger
    #
    filename = os.path.join(os.getcwd(), 'data', f'{func.__name__}.log')
    print(f'logfile: {filename}')
    logging.basicConfig(filename=filename, level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            # 'ran with args: {} and kwargs: {}'.format(args, kwargs)
            f'ran with args: {args} and kwargs: {kwargs}'
        )
        return func(*args, **kwargs)

    return wrapper


# @mylogger
# def display():
#     print('display function ran')


@mylogger
def displayinfo(name, age):
    print(f'displayinfo ran with arguments ({name}, {age})')


# display()
displayinfo('john', 25)
