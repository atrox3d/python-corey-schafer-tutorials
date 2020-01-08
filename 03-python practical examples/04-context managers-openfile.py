from contextlib import contextmanager
from modules import utils


def logmethod(fn):
    def wrapped(*args, **kwargs):
        print(f'entering {fn.__name__}')
        value = fn(*args, **kwargs)
        print(f'exiting {fn.__name__}')
        return value

    return wrapped


class OpenFile:
    @logmethod
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    @logmethod
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    @logmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile(utils.getdatafilepath('sample.txt'), 'w') as f:
    f.write('testing contex manager class')

print(f.closed)


@contextmanager
def openfile(file, mode='r'):
    print(f'opening file: {file} with mode: {mode}')
    f = open(file, mode)
    print(f'yielding file: {file}')
    yield f
    print(f'closing file: {file}')
    f.close()


with openfile(utils.getdatafilepath('sample.txt'), 'r+') as f:
    f.seek(0, 2)
    f.write('\ntesting contex manager function')

print(f.closed)
