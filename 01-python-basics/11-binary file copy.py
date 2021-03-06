#
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#
#   Python Tutorial: File Objects - Reading and Writing to Files
#
#################################################################################
from modules import utils

#os.chdir(os.path.join(os.getcwd(), 'data'))

"""
try to copy binary file in text mode
"""
utils.banner('try to copy binary file in text mode')
try:
    #
    #   open source file for reading
    #
    with open('../data/bronx.jpg', 'r') as rf:
        #
        #   open dest file for writing
        #
        with open('../data/bronx.copy.jpg', 'w') as wf:
            for line in rf:
                wf.write(line)
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')

"""
try to copy binary file in binary mode  line by line
"""
utils.banner('try to copy binary file in binary mode line by line')
try:
    #
    #   open source file for reading
    #
    with open('../data/bronx.jpg', 'rb') as rf:
        #
        #   open dest file for writing
        #
        with open('../data/bronx.copy.jpg', 'wb') as wf:
            for line in rf:
                wf.write(line)
except UnicodeDecodeError as ude:
    print(f'cannot read binary file : {ude}')

"""
try to copy binary file in binary mode  chunk by chunk
"""
utils.banner('try to copy binary file in binary mode chunk by chunk')
#
#   open source file for reading
#
with open('../data/bronx.jpg', 'rb') as rf:
    #
    #   open dest file for writing
    #
    with open('../data/bronx.copy.chunk.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        # check if we read something
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
