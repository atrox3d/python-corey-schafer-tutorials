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
logger = logging.getLogger(__name__)  # get local logger
logger.setLevel(logging.DEBUG)  # set logger level >= INFO
"""
########################################################################################################################
    - GET SAME FORMATTER INSTANCE FOR ALL HANDLERS
########################################################################################################################
"""
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)-10s | %(name)s | RemovalService.%(funcName)s | %(message)s')  # get formatter
"""
########################################################################################################################
    - GET CLI HANDLER INSTANCE
    - SET FORMATTER FOR CLI HANDLER INSTANCE
    - ADD HANDLER TO LOCAL LOGGER
########################################################################################################################
"""
cli_handler = logging.StreamHandler()  # get CLI handler (default=stderr)
cli_handler.setFormatter(formatter)  # set formatter for CLI handler
logger.addHandler(cli_handler)  # add CLI handler to logger


class RemovalService(object):
    """A service for removing objects from the filesystem."""

    def rm(self, filename):
        logger.info(f'check file {filename!r}')
        if os.path.isfile(filename):
            logger.info(f'{filename!r} exists')
            logger.info(f'call os.remove({filename!r})')
            os.remove(filename)
        else:
            logger.error(f'{filename!r} does not exists')


class UploadService(object):

    def __init__(self, removal_service):
        self.removal_service = removal_service

    def upload_complete(self, filename):
        self.removal_service.rm(filename)


if __name__ == '__main__':
    rs = RemovalService()
    rs.rm('NonExistingFile')
