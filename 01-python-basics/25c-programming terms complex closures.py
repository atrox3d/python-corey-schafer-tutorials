#
#   https://www.youtube.com/watch?v=swU3c34d2NQ
#
#   Programming Terms: Closures - How to Use Them and Why They Are Useful
#
#################################################################################
from modules import utils
import logging
import os

#################################################################################
utils.banner('closures: setup logging')

logfile = os.path.join(utils.PROJECT_PATH, 'data', 'example.log')
logging.basicConfig(
    filename=logfile,
    level=logging.INFO
)


def logger(func):
    #
    #   create logfunc
    #   will remeber func
    #   will run func(*args) after logging the call
    #
    def logfunc(*args):
        #
        #   log function call and arguments
        #
        logging.info('running "{}" with arguments {}'.format(func.__name__, args))
        #
        #   execute func and print return value
        #
        print(func(*args))

    return logfunc


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


#
#   create two decorators
#
addlogger = logger(add)
sublogger = logger(sub)
#
#   run them and check console/log file
#
addlogger(5, 5)
sublogger(5, 5)
