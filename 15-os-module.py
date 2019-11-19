#
#   https://www.youtube.com/watch?v=tJxcKyFMTGo
#
#################################################################################
import os


def hashline(width=80):
    print("#" * width)


hashline(160)
print(dir(os))
hashline(160)

# where are we
print('current dir: ', os.getcwd())
# get user homedirectory, system independent
homedirectory = os.path.expanduser('~')
# add desktop to home, system independent
desktop = os.path.join(homedirectory, 'desktop')
os.chdir(desktop)
print('current dir: ', os.getcwd())
