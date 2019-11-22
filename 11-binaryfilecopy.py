#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import utils
import io
import datetime

"""
try to copy binary file in text mode
"""
utils.banner('try to copy binary file in text mode')
try:
    #
    #   open source file for reading
    #
    with open('bronx.jpg', 'r' ) as rf:
        #
        #   open dest file for writing
        #
        with open('bronx.copy.jpg', 'w') as wf:
            for line in rf:
                wf.write(line)
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')

"""
try to copy binary file in binary mode
"""
utils.banner('try to copy binary file in binary mode')
try:
    #
    #   open source file for reading
    #
    with open('bronx.jpg', 'rb') as rf:
        #
        #   open dest file for writing
        #
        with open('bronx.copy.jpg', 'wb') as wf:
            for line in rf:
                wf.write(line)
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')




