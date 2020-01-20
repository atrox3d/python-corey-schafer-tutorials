"""
https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""
import os
import logging

"""
########################################################################################################################
    - GET LOCAL (NON-ROOT) LOGGER INSTANCE
    - SET LEVEL TO INFO (DEFAULT IS WARNING)
########################################################################################################################
"""
logger = logging.getLogger(__name__)    # get local logger
logger.setLevel(logging.DEBUG)          # set logger level >= INFO
"""
########################################################################################################################
    - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
########################################################################################################################
"""
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:RemovalService.%(funcname)s:%(message)s')  # get formatter
"""
########################################################################################################################
    - GET CLI HANDLER INSTANCE
    - SET FORMATTER FOR CLI HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
########################################################################################################################
"""
cli_handler = logging.StreamHandler()   # get CLI handler (default=stderr)
cli_handler.setFormatter(formatter)     # set formatter for CLI handler
logger.addHandler(cli_handler)          # add CLI handler to logger


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        print(f'{__class__.__name__}.{self.rm.__name__}|check file {filename!r}')
        if os.path.isfile(filename):
            print(f'{__class__.__name__}.{self.rm.__name__}|{filename!r} exists')
            print(f'{__class__.__name__}.{self.rm.__name__}|call os.remove({filename!r})')
            os.remove(filename)
        else:
            print(f'{__class__.__name__}.{self.rm.__name__}|{filename} does not exists')
