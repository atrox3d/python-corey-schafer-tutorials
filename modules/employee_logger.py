"""
https://www.youtube.com/watch?v=pd-0G0MigUA
"""

# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
#   (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
import logging
import sqlite3
from modules import utils
"""
    - SET LOGFILE PATH
    - DISPLAY IT
"""
logfile = utils.getdatafilepath(__file__ + '.log')                                  # set logfile path
print(logfile)
"""
    - GET LOCAL (NON-ROOT) LOGGER INSTANCE
    - SET LEVEL TO INFO (DEFAULT IS WARNING)
"""
logger = logging.getLogger(__name__)                                                # get local logger
logger.setLevel(logging.INFO)                                                       # set logger level >= INFO
"""
    - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
"""
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')     # get formatter
"""
    - GET FILE HANDLER INSTANCE
    - SET FORMATTER FOR FILE HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
"""
file_handler = logging.FileHandler(logfile)                                         # get file handler
file_handler.setFormatter(formatter)                                                # set formatter for file handler
logger.addHandler(file_handler)                                                     # add file handler to logger
"""
    - GET CLI HANDLER INSTANCE
    - SET FORMATTER FOR CLI HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
"""
cli_handler = logging.StreamHandler()                                               # get CLI handler (default=stderr)
cli_handler.setFormatter(formatter)                                                 # set formatter for CLI handler
logger.addHandler(cli_handler)                                                      # add CLI handler to logger

# logging.basicConfig(
#     level=logging.DEBUG,  # INFO ad above
#     filename=logfile,  # log on file
#     format='%(asctime)s:%(levelname)s:%(name)s:%(message)s'  # date time, level name, message
# )


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)


emp1 = Employee('luke', 'skywalker', 2000)
emp2 = Employee('obi', 'wankenoby', 2000)
