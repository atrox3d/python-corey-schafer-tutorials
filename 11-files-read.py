#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import utils

utils.banner('basic file open with builtin open()')
"""
- opens file in bssic mode and print some infos
- closes the file
- deletes the file variable
"""
f = open('data/test.txt', 'r')
print(f'file name : {f.name}')
print(f'file mode : {f.mode}')
print(f'file {f.name} is {"closed" if f.closed else "open"}')
f.close()
print(f'file {f.name} is {"closed" if f.closed else "open"}')
del f

"""
same as before but using context manager
"""
utils.banner('file open with context manager')
with open('data/test.txt', 'r') as f:
    print(f'file name : {f.name}')
    print(f'file mode : {f.mode}')

# the f variable is still available
print(f'file {f.name} is {"closed" if f.closed else "open"}')

"""
loads entire file in memory and print its contents with read() method
* not advisable with large files *
"""
utils.banner('print file contents loading all the file in memory with .read()')
with open('data/test.txt', 'r') as f:
    f_content = f.read()
    print(f_content)

"""
loads entire file in memory and print its contents with .readlines() method
* not advisable with large files *
"""
utils.banner('print file contents loading all the file in memory with .readlines()')
with open('data/test.txt', 'r') as f:
    f_content = f.readlines()
    print(f_content)

"""
loads a single line \\n terminated
the file pointer is consistent across multiple calls
"""
utils.banner('print file contents loading one line at a time with .readline()')
with open('data/test.txt', 'r') as f:
    f_content = f.readline()
    print(f_content)

    f_content = f.readline()
    print(f_content)

"""
loads a single line \\n terminated
the file pointer is consistent across multiple calls
"""
utils.banner('print file contents loading one line at a time with iterator')
with open('data/test.txt', 'r') as f:
    for line in f:
        print(line)

"""
reads data chunks of <size>
prints the resulting text
adds a symbol '*' to highlight the chunks
"""
utils.banner('print file contents loading chunks of data, using .read(size)')
with open('data/test.txt', 'r') as f:
    size = 10
    f_content = f.read(size)

    # while f_content:
    # while len(f_content):
    while len(f_content) > 0:
        print(f_content, end='*')
        f_content = f.read(size)

"""
moves the file pointer and prints:
current file pointer offset
data read at the offset
"""
utils.banner('print file contents changing file pointer position')
with open('data/test.txt', 'r') as f:
    size = 10
    for offset in range(1, size+1):
        print(f'current file pointer position: {f.tell()}')
        f_content = f.read(size)
        print(f_content)
        f.seek(offset)


