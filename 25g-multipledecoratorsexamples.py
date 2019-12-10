#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#################################################################################
from modules import utils
#
#   necessary to preserve original function with multiple decorators
#
from functools import wraps

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

    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(
            # 'ran with args: {} and kwargs: {}'.format(args, kwargs)
            f'ran with args: {args} and kwargs: {kwargs}'
        )
        return func(*args, **kwargs)

    return wrapper


#################################################################################
utils.banner('decorator practical examples: timer')


def mytimer(func):
    import time

    @wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        t = t2 - t1
        print(f'{func.__name__} ran in {t} secs')
        return result

    return wrapper


import time


#
#   without wraps this creates wrapper log, because it would be equal to :
#
#   displayinfo = mylogger(mytimer(displayinfo))
#
#   and mylogger would receive as argument the wrap inner function of mytimer
#
@mylogger
@mytimer
def displayinfo(name, age):
    time.sleep(1)
    print(f'displayinfo ran with arguments ({name}, {age})')


displayinfo('john', 25)
