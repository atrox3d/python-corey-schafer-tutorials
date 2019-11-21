#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import utils

utils.banner('basic file open with builtin open()')
f = open('test.txt', 'r')
print(f'file name : {f.name}')
print(f'file mode : {f.mode}')
print(f'file {f.name} is {"closed" if f.closed else "open"}')
f.close()
print(f'file {f.name} is {"closed" if f.closed else "open"}')
del f

utils.banner('file open with context manager')
with open('test.txt', 'r') as f:
    print(f'file name : {f.name}')
    print(f'file mode : {f.mode}')

# the f variable is still available
print(f'file {f.name} is {"closed" if f.closed else "open"}')

utils.banner('print file contents loading all the file in memory')
with open('test.txt', 'r') as f:
    f_content = f.read()
    print(f_content)

utils.banner('print file contents loading all the file in memory')
with open('test.txt', 'r') as f:
    f_content = f.readlines()
    print(f_content)

utils.banner('print file contents loading one line at a time with readline')
with open('test.txt', 'r') as f:
    """
    loads a single line \\n terminated
    the file pointer is consistent across multiple calls
    """
    f_content = f.readline()
    print(f_content)

    f_content = f.readline()
    print(f_content)

utils.banner('print file contents loading one line at a time with iterator')
with open('test.txt', 'r') as f:
    """
    loads a single line \\n terminated
    the file pointer is consistent across multiple calls
    """
    for line in f:
        print(line)

utils.banner('print file contents loading chunks of data')
with open('test.txt', 'r') as f:
    """
    reads data chunks of <size>
    prints the resulting text
    adds a symbol 
    """
    size = 10
    f_content = f.read(size)

    # while f_content:
    # while len(f_content):
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size)

utils.banner('print file contents changing file pointer position')
with open('test.txt', 'r') as f:
    """
    """
    size = 10
    f_content = f.read(size)
    print(f.tell())
    print(f_content, end='')
    f.seek(0)
    print(f_content, end='')


