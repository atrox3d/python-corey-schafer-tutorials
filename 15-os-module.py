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
# expand windows %userprofile% variable
homedirectory = os.path.expandvars('%userprofile%')
# add desktop
os.chdir(homedirectory + '\\desktop')
print('current dir: ', os.getcwd())




