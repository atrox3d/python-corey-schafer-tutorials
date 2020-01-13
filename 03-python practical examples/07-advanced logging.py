#
#   https://youtu.be/jxmzY9soFXg
#
#########################################################################################################
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
#     (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
import logging
from modules import utils
#########################################################################################################
#
#   this module creates another root logger that has precedence over the local root logger
#   as a consequence the output of this script goes to the employee_logger's log file
#
#########################################################################################################
from modules import employee_logger


logfile = utils.getdatafilepath(__file__ + '.log')
print(logfile)

logging.basicConfig(
    level=logging.DEBUG,                                # all levels
    filename=logfile,                                   # log on file
    format='%(asctime)s:%(levelname)s:%(message)s'      # date time, level name, message
)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
