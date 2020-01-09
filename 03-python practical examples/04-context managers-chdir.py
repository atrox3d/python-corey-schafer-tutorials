import os
from contextlib import contextmanager
from modules import utils


# def logmethod(fn):
#     def wrapped(*args, **kwargs):
#         print(f'entering {fn.__name__}')
#         value = fn(*args, **kwargs)
#         print(f'exiting {fn.__name__}')
#         return value
#
#     return wrapped
#
#
# class OpenFile:
#     @logmethod
#     def __init__(self, filename, mode='r'):
#         self.filename = filename
#         self.mode = mode
#
#     @logmethod
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     @logmethod
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with OpenFile(utils.getdatafilepath('sample.txt'), 'w') as f:
#     f.write('testing contex manager class')


@contextmanager
def chdir(destination):
    try:
        cwd = os.getcwd()
        print(f'changing current directory to {destination}')
        os.chdir(destination)
        newcwd = os.getcwd()
        print(f'yielding newcwd: {newcwd}')
        yield newcwd
    finally:
        print(f'changing back to {cwd} direcory')
        os.chdir(cwd)


