#
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#
#   Python Tutorial: File Objects - Reading and Writing to Files
#
#################################################################################
from modules import utils

#os.chdir(os.path.join(os.getcwd(), 'data'))

#################################################################################
# try to copy binary file in text mode
#################################################################################
utils.banner('try to copy binary file in text mode')
try:
    with open('../data/bronx.jpg', 'r') as rf:              # open source file for reading
        with open('../data/bronx.copy.jpg', 'w') as wf:     # open dest file for writing
            for line in rf:                                 # read each line from rf
                wf.write(line)                              # andwrite it on wf
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')

#################################################################################
# try to copy binary file in binary mode  line by line
#################################################################################
utils.banner('try to copy binary file in binary mode line by line')
try:
    with open('../data/bronx.jpg', 'rb') as rf:             # open source file for reading
        with open('../data/bronx.copy.jpg', 'wb') as wf:    # open dest file for writing
            for line in rf:                                 # read each line from rf
                wf.write(line)                              # andwrite it on wf
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')

#################################################################################
# try to copy binary file in binary mode  chunk by chunk
#################################################################################
utils.banner('try to copy binary file in binary mode chunk by chunk')
with open('../data/bronx.jpg', 'rb') as rf:                 # open source file for reading
    with open('../data/bronx.copy.chunk.jpg', 'wb') as wf:  # open dest file for writing
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)                      # read first chunk
        while len(rf_chunk) > 0:                            # check if we read something
            wf.write(rf_chunk)                              # write chunk
            rf_chunk = rf.read(chunk_size)                  # read next chunk
