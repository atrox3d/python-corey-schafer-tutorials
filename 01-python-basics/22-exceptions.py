#
#   https://www.youtube.com/watch?v=NIWwJbo-9_8
#
#################################################################################
import os
from modules import utils


corruptfilepath = os.path.join(utils.PROJECT_PATH, 'data', 'corrupt_file.txt')
datafilepath = os.path.join(utils.PROJECT_PATH, 'data', 'test_file.txt')
wrongdatafilepath = os.path.join(utils.PROJECT_PATH, 'data', 'testfile.txt')

try:
    f = open(corruptfilepath)
    name = os.path.basename(f.name)
    if name == 'corrupt_file.txt':
        print('raising')
        raise Exception
except FileNotFoundError as e:
    """
    more specific first
    """
    print(e)
except Exception as e:
    """
    less specific after
    """
    print('error')
else:
    """
    everything went ok
    """
    print(f.read())
    f.close()
finally:
    """
    no matter the outcome
    """
    print('executing finally')


