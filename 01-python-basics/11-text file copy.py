#
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#
#   Python Tutorial: File Objects - Reading and Writing to Files
#
#################################################################################
from modules import utils

#################################################################################
# try to write on an open for reading file
#################################################################################
utils.banner('copy files')
with open('../data/test.txt', 'r') as rf:               # open source file for reading

    print(f'dump of {rf.name}')
    utils.hashline(char='-')
    for line in rf:                                     # show source file contents
        print(line, end='')
    utils.hashline(char='-')

    rf.seek(0)                                          # reset rf file pointer

    with open('../data/test.copy.txt', 'w') as wf:      # open dest file for writing
        for line in rf:                                 # read over each line of rf
            wf.write(line)                              # writes every line in wf

    with open('../data/test.copy.txt', 'r') as wf:      # open dest file for reading
        print(f'dump of {wf.name}')
        utils.hashline(char='-')
        for line in wf:                                 # show dest file contents
            print(line, end='')
        utils.hashline(char='-')



