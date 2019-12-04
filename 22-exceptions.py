#
#   https://www.youtube.com/watch?v=NIWwJbo-9_8
#
#################################################################################
import utils
import os

datafilepath = os.path.join(os.getcwd(), 'data', 'test_file.txt')
wrongdatafilepath = os.path.join(os.getcwd(), 'data', 'testfile.txt')

try:
    f = open(datafilepath)
except FileNotFoundError as e:
    """
    more specific first
    """
    print(e)
except Exception as e:
    """
    less specific after
    """
    print(e)
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


