from modules import utils


class OpenFile:

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


with OpenFile(utils.getdatafilepath('sample.txt'), 'w') as f:
    f.write('testing contex manager')

print(f.closed)
