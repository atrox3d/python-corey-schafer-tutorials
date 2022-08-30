#
#   https://www.youtube.com/watch?v=tJxcKyFMTGo
#
#   Python Tutorial: OS Module - Use Underlying Operating System Functionality
#
#################################################################################
import os


def hashline(width=160, char='#'):
    print(char * width)


def banner(text, height=3, width=160, char='#'):
    hashline(width, char)
    spacing = height // 2 + 1
    for spaceline in range(1, spacing):
        print(char)
    print(f'{char} {text}')
    for spaceline in range(1, spacing):
        print(char)
    hashline(width, char)


banner("dir(os)")
print(dir(os))
"""

change directory

"""
banner("os.getcwd")
# where are we
print('current dir: ', os.getcwd())
# get user homedirectory, os independent
homedirectory = os.path.expanduser('~')
# add desktop to home, os independent
desktop = os.path.join(homedirectory, 'desktop')
os.chdir(desktop)
print('current dir: ', os.getcwd())
"""

list directory contents

"""
banner("os.listdir")
print(os.listdir())
"""

create directories

"""
banner("create dirs")
try:
    # create os independent path
    test_sub = os.path.join('test', 'sub')
    # try to create path, will fail.
    os.mkdir(test_sub)
except FileNotFoundError as fnfe:
    print('os.mkdir doesnt create multiple levels:', fnfe)
except FileExistsError as fee:
    # silent fail if test exists already
    pass

# create multiple level path, ignore existing
os.makedirs(test_sub, exist_ok=True)
print(os.listdir())
"""

delete directories

"""
banner('delete dirs')
# this deletes only the last folder in the path
os.rmdir(test_sub)
try:
    # this will fail, due to the rmdir
    os.removedirs(test_sub)
except FileNotFoundError as fnfe:
    print(f'cannot delete {test_sub}: {fnfe}')
    os.removedirs('test')
hashline(char='-')
print(os.listdir())
"""

rename files

"""
banner('os.rename')
# create test file
open('../data/test.txt', 'a').close()
os.rename('../data/test.txt', 'demo.txt')
print(os.listdir())
os.rename('demo.txt', '../data/test.txt')
hashline(char='-')
print(os.listdir())
"""

file info

"""
banner('os.stat')
stats = os.stat('../data/test.txt')
print(type(stats))

# vars(stats) does not work
for k, v in {name: getattr(stats, name) for name in dir(stats) if name.startswith('st_')}.items():
    print(f'{k:<20}|{str(type(v)):<20}:{v:>20}')

from datetime import datetime
modification_time = os.stat('../data/test.txt').st_mtime
print('modification time : ', datetime.fromtimestamp(modification_time))

banner("os.walk")
os.chdir(desktop)
print(os.getcwd())

for dirpath, dirnames, filenames in os.walk(desktop):
    print('current path: ', dirpath)
    print('directories : ', dirnames)
    print('files       : ', filenames)
    print()

banner('environment variables')
print(type(os.environ))
for k, v in os.environ.items():
    # if not isinstance(v, str):
    #     print(f'element {v} is not string: {str(type(v))}')
    #     break
    print(f'{k:<30} |{str(type(v))} : {v}')

hashline()
print(os.environ)
hashline()
print(os.environ.get('HOME', 'no HOME variable defined'))

banner('os.path')
temptxt = os.path.join(desktop, 'temp.txt')
print('full path: ', temptxt)
print('basename : ', os.path.basename(temptxt))
print('dirname  : ', os.path.dirname(temptxt))
print('split    : ', os.path.split(temptxt))
dirname, filename = os.path.split(temptxt)
print(dirname, filename)
print('split ext: ', os.path.splitext(temptxt))
filepath, fileext = os.path.splitext(temptxt)
print(filepath, fileext)
# finally
dirname, filename = os.path.split(temptxt)
filename, fileext = os.path.splitext(os.path.basename(temptxt))
print(dirname, filename, fileext)
hashline(char='-')

print(temptxt, "" if os.path.exists(temptxt) else "doesn't", "exists")
print(desktop, "is" if os.path.isdir(desktop) else "is not", "a directory")
print(desktop, "is" if os.path.isfile(desktop) else "is not", "a file")
