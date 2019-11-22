#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import utils
import io
import datetime

"""
try to write on an open for reading file
"""
utils.banner('copy files')
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




