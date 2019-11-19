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
    test_sub = os.path.join('test','sub')
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


