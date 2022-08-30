#
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#
#   Python Tutorial: File Objects - Reading and Writing to Files
#
#################################################################################
from modules import utils

utils.banner('basic file open with builtin open()')
f = open('../data/test.txt', 'r')                       # opens file in basic mode
print(f'file name : {f.name}')                          # print some infos
print(f'file mode : {f.mode}')
print(f'file {f.name} is ' +
      f'{"closed" if f.closed else "open"}')
f.close()                                               # closes the file
print(f'file {f.name} is ' +
      f'{"closed" if f.closed else "open"}')
del f                                                   # deletes the file variable


utils.banner('file open with context manager')
with open('../data/test.txt', 'r') as f:                # opens file with context manager
    print(f'file name : {f.name}')                      # print some infos
    print(f'file mode : {f.mode}')
print(f'file {f.name} is ' +
      f'{"closed" if f.closed else "open"}')            # f variable is still available


#################################################################################
# * not advisable with large files *
#################################################################################
utils.banner('print file contents loading all the file in memory with .read()')
with open('../data/test.txt', 'r') as f:                # opens file with context manager
    f_content = f.read()                                # loads entire file in memory
    print(f_content)                                    # print its contents

#################################################################################
# * not advisable with large files *
#################################################################################
utils.banner('print file contents loading all the file in memory with .readlines()')
with open('../data/test.txt', 'r') as f:                # opens file with context manager
    f_content = f.readlines()                           # loads entire file in memory
    print(f_content)                                    # print its contents

utils.banner('print file contents loading one line at a time with .readline()')
with open('../data/test.txt', 'r') as f:                # opens file with context manager
    f_content = f.readline()                            # loads a single line \\n terminated
    print(f_content)

    f_content = f.readline()                            # the file pointer is consistent across multiple calls
    print(f_content)

utils.banner('print file contents loading one line at a time with iterator')
with open('../data/test.txt', 'r') as f:
    for line in f:                                      # loads a single line \\n terminated
        print(line)                                     # the file pointer is consistent across multiple calls

utils.banner('print file contents loading chunks of data, using .read(size)')
with open('../data/test.txt', 'r') as f:
    size = 10
    f_content = f.read(size)                            # reads data chunks of <size>

    # while f_content:
    # while len(f_content):
    while len(f_content) > 0:
        print(f_content, end='*')                       # prints the resulting text,
                                                        # adds a symbol '*' to highlight the chunks
        f_content = f.read(size)                        # reads data chunks of <size>


utils.banner('print file contents changing file pointer position')
with open('../data/test.txt', 'r') as f:
    size = 10
    for offset in range(1, size+1):                     # loop from 1 to 10
        print(f'current file pointer position:' +
              f'{f.tell()}')
        print(f"f_content = f.read({size})")
        f_content = f.read(size)                        # read chunk of 10
        print(f'current file pointer position:' +
              f'{f.tell()}')
        print(f_content)
        f.seek(offset)                                  # moves the file pointer


