#
#   https://www.youtube.com/watch?v=tJxcKyFMTGo
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
open('test.txt', 'a').close()
os.rename('test.txt', 'demo.txt')
print(os.listdir())
os.rename('demo.txt', 'test.txt')
hashline(char='-')
print(os.listdir())
"""

file info

"""
banner('os.stat')
stats = os.stat('test.txt')
print(type(stats))

# vars(stats) does not work
for k, v in {name: getattr(stats, name) for name in dir(stats) if name.startswith('st_')}.items():
    print(f'{k:<20}|{str(type(v)):<20}:{v:>20}')

from datetime import datetime
modification_time =  os.stat('test.txt').st_mtime
print('modification time : ', datetime.fromtimestamp(modification_time))

banner("os.walk")
os.chdir(desktop)
print(os.getcwd())

for dirpath, dirnames, filenames in os.walk(desktop):
    print('current path: ', dirpath)
    print('directories : ', dirnames)
    print('files       : ', filenames)
    print()




