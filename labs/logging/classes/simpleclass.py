from modules import logger

"""
    module level logger
"""
modulelogger = logger.getCLIlogger()
modulelogger.info('format: {}'.format(modulelogger.handlers[0].formatter._fmt))


class SimpleClass:
    classlogger = logger.getCLIlogger('classlogger')
    modulelogger.info('class')
    classlogger.info('class')

    def __init__(self, value='default'):
        self.value = value
        """
        instance level logger
        """
        modulelogger.info(value)
        self.classlogger.info(value)
        self.instancelogger = logger.getCLIlogger('instancelogger')
        self.instancelogger.info(value)


if __name__ == '__main__':
    sc = SimpleClass()
