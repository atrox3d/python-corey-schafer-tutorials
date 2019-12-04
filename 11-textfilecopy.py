#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
from modules import utils

"""
try to write on an open for reading file
"""
utils.banner('copy files')
#
#   open source file for reading
#
with open('data/test.txt', 'r') as rf:
    #
    #   show source file contents
    #
    print(f'dump of {rf.name}')
    utils.hashline(char='-')
    for line in rf:
        print(line, end='')
    utils.hashline(char='-')
    # reset rf file pointer
    rf.seek(0)
    #
    #   open dest file for writing
    #
    with open('data/test.copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

    #
    #   open dest file for reading
    #
    with open('data/test.copy.txt', 'r') as wf:
        print(f'dump of {wf.name}')
        utils.hashline(char='-')
        for line in wf:
            print(line, end='')
        utils.hashline(char='-')



