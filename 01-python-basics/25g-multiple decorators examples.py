#
#   https://www.youtube.com/watch?v=FsAPt_9Bf3U
#
#   Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
#
#################################################################################
from modules import utils
import time
#
#   necessary to preserve original function with multiple decorators
#
from functools import wraps

#################################################################################
utils.banner('decorator practical examples: logger')


def mylogger(func):
    import logging
    import os

    filename = os.path.join(                            # create logfile path
        utils.PROJECT_PATH,
        'data',
        f'{func.__name__}.log'
    )
    print(f'mylogger        | logfile: {filename}')
    logging.basicConfig(                                 # configure logger
        filename=filename,
        level=logging.INFO
    )

    # @wraps(func)                                      # commented out to show call stack
    def mylogger_wrapper(*args, **kwargs):
        logging.info(                                   # log execution
            f'running with args    | '
            f'{args} and kwargs: {kwargs}'
        )
        print(                                          # echoes execution
            f'mylogger        | mylogger_wrapper | '
            f'running {func.__name__} with args: '
            f'{args} and kwargs: {kwargs}'
        )
        return func(*args, **kwargs)                    # executes func

    return mylogger_wrapper                             # returns wrapper


#################################################################################
utils.banner('decorator practical examples: timer')


def mytimer(func):
    import time

    # @wraps(func)                                      # commented out to show call stack
    def mytimer_wrapper(*args, **kwargs):
        t1 = time.time()                                # saves timer1
        result = func(*args, **kwargs)                  # executes func and saves result
        t2 = time.time()                                # saves timer2
        t = t2 - t1                                     # calcs time difference
        print(                                          # echoes execution
            f'mytimer_wrapper | wrapper          | '
            f'{func.__name__} ran in {t} secs'
        )
        return result                                   # returns saved result
    return mytimer_wrapper                              # returns wrapper


#
#   without @wraps this creates wrapper log, because it would be equal to :
#   displayinfo = mylogger(mytimer(displayinfo))
#   and mylogger would receive as argument the wrap inner function of mytimer
#
@mylogger                                               # mylogger will run mytimer
@mytimer                                                # mytimer will run displayinfo
def displayinfo(name, age):
    time.sleep(1)
    print(f'displayinfo     | running with arguments ({name}, {age})')


displayinfo('john', 25)
