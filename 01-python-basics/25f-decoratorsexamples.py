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

#################################################################################
utils.banner('decorator practical examples: timer')


def mytimer(func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print(f'{func.__name__} ran in {t} secs')
        return result

    return wrapper


import time


@mytimer
def displayinfo(name, age):
    time.sleep(1)
    print(f'displayinfo ran with arguments ({name}, {age})')


displayinfo('john', 25)
