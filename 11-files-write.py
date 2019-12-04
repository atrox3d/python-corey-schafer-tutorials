#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
from modules import utils
import io
import datetime

"""
try to write on an open for reading file
"""
utils.banner('try to write on an open for reading file')
try:
    with open('data/test.txt', 'r') as f:
        f.write('cannot write file open for read')
except io.UnsupportedOperation as iuo:
    print(f'couldnt write to {f.name}: {iuo}')

"""
create new file for writing
"""
utils.banner('create new file for writing')
#
#   creates file without writing anything
#
with open('data/test2.txt', 'w') as f:
    pass

with open('data/test2.txt', 'w') as f:
    stardate = datetime.datetime.now().strftime("[%d/%m/%y %H:%M]")
    text = f'{stardate} - write to file test'
    # print(text)
    f.write(text)

    #
    #   file is not yet updated
    #   doesnt read anything
    #
    with open('data/test2.txt', 'r') as rf:
        checktext = rf.read()
        print(checktext)

    # appends the same string
    f.write(text)

with open('data/test2.txt', 'r') as rf:
    checktext = rf.read()
    print(checktext)

utils.banner('overwrite using seek')
"""
write using seek
"""
with open('data/test2.txt', 'w') as f:
    stardate = datetime.datetime.now().strftime("[%d/%m/%y %H:%M]")
    text = f'{stardate} - write to file test'
    # print(text)
    f.write(text)

    # overwrites the same string
    f.seek(0)
    f.write(text)

    # overwrites just one char
    f.seek(0)
    f.write('*')

with open('data/test2.txt', 'r') as rf:
    checktext = rf.read()
    print(checktext)
