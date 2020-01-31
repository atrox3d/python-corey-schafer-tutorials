from os.path import basename
thisfile = basename(__file__)

if __name__ == '__main__':
    print(f'{thisfile} | hello, you are runnig this file with __name__={__name__}')
else:
    print(f'{thisfile} | hello, is being executed on import with __name__={__name__}')
