import os
from contextlib import contextmanager
from modules import utils


def logmethod(fn):
    def wrapped(*args, **kwargs):
        print(f'entering {fn.__name__}')
        value = fn(*args, **kwargs)
        print(f'exiting {fn.__name__}')
        return value

    return wrapped


class Chdir:
    @logmethod
    def __init__(self, destination):
        self.width = 30
        self.destination = destination
        self.cwd = os.getcwd()
        print(f'{"saving current dir":<{self.width}}: {self.cwd}')

    @logmethod
    def __enter__(self):
        print(f'{"changing current dir to":<{self.width}}: {self.destination}')
        os.chdir(self.destination)
        self.newcwd = os.getcwd()

    @logmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'{"changing back to dir":<{self.width}}: {self.cwd}')
        os.chdir(self.cwd)


#
#
# with OpenFile(utils.getdatafilepath('sample.txt'), 'w') as f:
#     f.write('testing contex manager class')


@contextmanager
def chdir(destination):
    width = 30
    cwd = os.getcwd()
    print(f'{"saving current dir":<{width}}: {cwd}')

    try:
        print(f'{"changing current dir to":<{width}}: {destination}')
        os.chdir(destination)
        newcwd = os.getcwd()
        print(f'{"yielding newcwd":<{width}}: {newcwd}')
        yield newcwd
    finally:
        print(f'{"changing back to dir":<{width}}: {cwd}')
        os.chdir(cwd)


with chdir(utils.PROJECT_PATH) as cd:
    print(os.listdir(cd))

with Chdir(utils.PROJECT_PATH) as cd:
    print(os.listdir(cd))

