#
#   https://www.youtube.com/watch?v=NIWwJbo-9_8
#
#   Python Tutorial: Using Try/Except Blocks for Error Handling
#
#################################################################################
import os
from modules import utils


corruptfilepath = os.path.join(utils.PROJECT_PATH, 'data', 'corrupt_file.txt')
datafilepath = os.path.join(utils.PROJECT_PATH, 'data', 'test_file.txt')
wrongdatafilepath = os.path.join(utils.PROJECT_PATH, 'data', 'testfile.txt')

try:
    f = open(corruptfilepath)                           # open fake corrupt file
    name = os.path.basename(f.name)                     # gest just the filename
    if name == 'corrupt_file.txt':                      # fake exception
        print('raising')
        raise Exception                                 # raise fake exception
except FileNotFoundError as e:                          # more specific first
    print(e)
except Exception as e:                                  # less specific after
    print('error')
else:                                                   # everything went ok, no exceptions
    print(f.read())
    f.close()
finally:
    print('executing finally')                          # no matter the outcome


