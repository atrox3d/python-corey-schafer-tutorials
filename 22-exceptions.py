#
#   https://www.youtube.com/watch?v=NIWwJbo-9_8
#
#################################################################################
import utils
import os

datafilepath = os.path.join(os.getcwd(), 'data', 'test_file.txt')
wrongdatafilepath = os.path.join(os.getcwd(), 'data', 'testfile.txt')

try:
    f = open(wrongdatafilepath)
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
