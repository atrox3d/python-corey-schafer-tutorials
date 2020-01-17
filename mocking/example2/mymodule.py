"""
https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""
import os


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

