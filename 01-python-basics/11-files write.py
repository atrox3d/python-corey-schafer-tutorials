#
#   https://www.youtube.com/watch?v=Uh2ebFW8OYM
#
#   Python Tutorial: File Objects - Reading and Writing to Files
#
#################################################################################
from modules import utils
import io
import datetime

utils.banner('try to write on an open for reading file')
try:
    with open('../data/test.txt', 'r') as f:
        f.write('cannot write file open for read')      # try to write on an open for reading file
except io.UnsupportedOperation as iuo:
    print(f'couldnt write to {f.name}: {iuo}')

utils.banner('create new file for writing')

with open('../data/test2.txt', 'w') as f:
    pass                                                # creates file without writing anything

with open('../data/test2.txt', 'w') as f:
    stardate = datetime.datetime.now()\
        .strftime("[%d/%m/%y %H:%M]")
    text = f'{stardate} - write to file test'
    f.write(text)                                       # write string to file

    with open('../data/test2.txt', 'r') as rf:          # file is not yet updated
        checktext = rf.read()                           # doesnt read anything
        print(f"checktext: {checktext}")                # OUTPUT | checktext:

    f.write(text)                                       # appends the same string

with open('../data/test2.txt', 'r') as rf:              # reopens file in read mode
    checktext = rf.read()                               # reads content

    # OUTPUT | checktext: [dd/mm/aa hh:mm] - write to file test[dd/mm/aa hh:mm] - write to file test
    print(f"checktext: {checktext}")

utils.banner('overwrite using seek')

with open('../data/test2.txt', 'w') as f:               # reopens file for writing
    stardate = datetime.datetime.now()\
        .strftime("[%d/%m/%y %H:%M]")
    text = f'{stardate} - write to file test'
    f.write(text)                                       # writes string to file

    f.seek(0)                                           # rewinds file pointer
    f.write(text)                                       # overwrites the same string

    f.seek(0)                                           # rewinds file pointer
    f.write('*')                                        # overwrites just one char

with open('../data/test2.txt', 'r') as rf:              # reopens file for reading
    checktext = rf.read()                               # reads all content
    # OUTPUT | checktext: *dd/mm/aa hh:mm] - write to file test
    print(f"checktext: {checktext}")
