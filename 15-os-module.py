#
#   https://www.youtube.com/watch?v=tJxcKyFMTGo
#
#################################################################################
import os


def hashline(width=160, char='#'):
    print(char * width)


hashline()
print(dir(os))
hashline()
"""

change directory

"""
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
hashline()
print(os.listdir())
"""

create directories

"""
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
hashline()
print(os.listdir())

hashline(char='-')
