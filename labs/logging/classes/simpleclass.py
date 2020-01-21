from modules import logger


"""
    module level logger
"""
modulelogger = logger.getCLIlogger()
modulelogger.info('hello')


class SimpleClass:
    classlogger = logger.getCLIlogger('classlogger')
    classlogger.info('class')

    def __init__(self, value='default'):
        self.value = value
        """
        instance level logger
        """
        self.instancelogger = logger.getCLIlogger('instancelogger')
        self.instancelogger.info(value)
        self.classlogger.info(value)
        modulelogger.info(value)


if __name__ == '__main__':
    sc = SimpleClass()
