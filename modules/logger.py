import os
import logging


# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
# (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

def getCLIlogger(classname=None):
    """
    ########################################################################################################################
        - GET LOCAL (NON-ROOT) LOGGER INSTANCE
        - SET LEVEL TO INFO (DEFAULT IS WARNING)
    ########################################################################################################################
    """
    if classname is not None:
        _defaultlogger = logging.getLogger(classname)  # get local logger
    else:
        _defaultlogger = logging.getLogger(__name__)  # get local logger

    _defaultlogger.setLevel(logging.DEBUG)  # set logger level >= INFO
    """
    ########################################################################################################################
        - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
    ########################################################################################################################
    """
    if classname is not None:
        formatstring = f'%(asctime)s | %(levelname)-10s | %(name)-20s | {classname}.%(funcName)s | %(message)s'
    else:
        formatstring = '%(asctime)s | %(levelname)-10s | %(name)-20s | %(funcName)s | %(message)s'

    formatter = logging.Formatter(formatstring)  # get formatter
    """
    ########################################################################################################################
        - GET CLI HANDLER INSTANCE
        - SET FORMATTER FOR CLI HANDLER INSTANCE
        - ADD HANDLER TO LOCAL LOGGER
    ########################################################################################################################
    """
    cli_handler = logging.StreamHandler()  # get CLI handler (default=stderr)
    cli_handler.setFormatter(formatter)  # set formatter for CLI handler
    _defaultlogger.addHandler(cli_handler)  # add CLI handler to logger

    return _defaultlogger


if __name__ == '__main__':
    logger = getCLIlogger()
    logger.debug('testing testing')
    logger.info('testing testing')
    logger.warning('testing testing')
    logger.error('testing testing')
    logger.critical('testing testing')

    logger = getCLIlogger('classname')
    logger.debug('testing testing')
    logger.info('testing testing')
    logger.warning('testing testing')
    logger.error('testing testing')
    logger.critical('testing testing')

    print(logger.handlers)
    print(logger.handlers[0])
    print(logger.handlers[0].formatter)
    print(logger.handlers[0].formatter._fmt)
