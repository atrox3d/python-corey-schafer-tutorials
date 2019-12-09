#
#   https://www.youtube.com/watch?v=swU3c34d2NQ
#
#################################################################################
from modules import utils
import logging
import os

#################################################################################
utils.banner('closures: setup logging')

logfile = os.path.join(os.getcwd(), 'data', 'example.log')
logging.basicConfig(
    filename=logfile,
    level=logging.INFO
)


def logger(func):
    #
    #   create logfunc
    #   will remeber func and args
    #   will run func(*args) after logging the call
    #
    def logfunc(*args):
        logging.info('running "{}" with arguments {}'.format(func.__name__, args))
        print(func(*args))

    return logfunc

