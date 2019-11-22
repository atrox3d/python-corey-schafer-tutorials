#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import utils
import io

"""
try to write on an open for reading file
"""
utils.banner('try to write on an open for reading file')
try:
    with open('test.txt', 'r') as f:
        f.write('cannot write file open for read')
except io.UnsupportedOperation as iuo:
    print(f'couldnt write to {f.name}: {iuo}')

