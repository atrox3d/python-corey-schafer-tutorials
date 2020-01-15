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
"""
########################################################################################################################
    - SET LOGFILE PATH
    - DISPLAY IT
########################################################################################################################
"""
logfile = utils.getdatafilepath(__file__ + '.log')                                  # set logfile path
print(logfile)
errorfile = utils.getdatafilepath(__file__ + '.error.log')                                  # set logfile path
print(errorfile)
"""
########################################################################################################################
    - GET LOCAL (NON-ROOT) LOGGER INSTANCE
    - SET LEVEL TO INFO (DEFAULT IS WARNING)
########################################################################################################################
"""
logger = logging.getLogger(__name__)                                                # get local logger
logger.setLevel(logging.DEBUG)                                                       # set logger level >= INFO
"""
########################################################################################################################
    - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
########################################################################################################################
"""
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')     # get formatter
"""
########################################################################################################################
    - GET FILE HANDLER INSTANCE
    - SET FORMATTER FOR FILE HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
########################################################################################################################
"""
file_handler = logging.FileHandler(logfile)                                         # get file handler
file_handler.setFormatter(formatter)                                                # set formatter for file handler
logger.addHandler(file_handler)                                                     # add file handler to logger
"""
########################################################################################################################
    - GET FILE HANDLER INSTANCE
    - SET FORMATTER FOR FILE HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
########################################################################################################################
"""
errorfile_handler = logging.FileHandler(errorfile)                                   # get file handler
errorfile_handler.setFormatter(formatter)                                            # set formatter for file handler
errorfile_handler.setLevel(logging.ERROR)
logger.addHandler(errorfile_handler)                                                 # add file handler to logger
"""
########################################################################################################################
    - GET CLI HANDLER INSTANCE
    - SET FORMATTER FOR CLI HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
########################################################################################################################
"""
cli_handler = logging.StreamHandler()                                               # get CLI handler (default=stderr)
cli_handler.setFormatter(formatter)                                                 # set formatter for CLI handler
logger.addHandler(cli_handler)                                                      # add CLI handler to logger

# logging.basicConfig(
#     level=logging.DEBUG,  # INFO ad above
#     filename=logfile,  # log on file
#     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'  # date time, level name, message
# )


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
    try:
        return x / y
    except ZeroDivisionError as zde:
        logger.error(zde)
        logger.exception(zde)
        # return zde


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
