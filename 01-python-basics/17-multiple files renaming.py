#
#   https://www.youtube.com/watch?v=ve2pmm5JqmI
#
#   Python Tutorial: Automate Parsing and Renaming of Multiple Files
#
#################################################################################
from modules import utils
import os


def remove_examplefiles(dirname):
    """
    delete existing example files
    :param dirname: example files directory
    :return:
    """
    utils.banner('DELETING EXISTING EXAMPLE FILES')
    files = os.listdir(dirname)                         # gets list of directory entries
    for f in files:                                     # for each entry
        f = os.path.join(dirname, f)                    # creates absolute path
        if os.path.isfile(f):                           # check if is a file
            print(f'deleting {f}')
            os.remove(f)                                # delete file
        else:
            print(f'skipping {f}')


def create_examplefiles(dirname):
    """
    create example files
    :param dirname:
    :param maxfile:
    :return:
    """

    utils.banner('CREATE EXAMPLE FILES')

    planets = {                                         # create set
        'earth',
        'jupiter',
        'mars',
        'mercury',
        'neptune',
        'pluto',
        'saturn',
        'uranus',
        'venus',
    }

    planetnum = 0
    for planet in planets:
        filename = f'{planet} - '\
                   f'our solar system - '\
                   f'#{planetnum}.mp4'                  # format each filename
        filepath = os.path.join(dirname, filename)      # add path
        print(f'creating : {filepath}')
        with open(filepath, 'w') as _:                  # create empty file
            pass
        planetnum += 1

    os.listdir(dirname)


#################################################################################
# start by creating the files
#################################################################################
exampledir = '../multifile'
if os.path.exists(exampledir):
    remove_examplefiles(exampledir)
    os.removedirs(exampledir)

os.makedirs(exampledir)                                 # create directory
create_examplefiles(exampledir)
#
#   check our new files
#
utils.banner(f'changing to {exampledir} directory and listing contents')
print('current directory: ', os.getcwd())
os.chdir(os.path.join(os.getcwd(), exampledir))
print('current directory: ', os.getcwd())

utils.hashline(char='-')
for file in os.listdir():
    print(file)
#
#   start parsing the filenames
#
##########################################################################################################
#
#   get max length of string representation of tuples
#
maxtuplelen = max(                                      # return max length

    map(                                                # returns a map of lengths

        lambda afile: len(                              # return the length of the string representation of the tuple
            str(                                        # convert tuple to string
                os.path.splitext(afile)                 # get tuple name, ext
            )
        ),
        os.listdir()                                    # for all files
    )
)
#
#   get max length of first string of tuples
#
maxfilenamelen = max(
    map(                                                # returns a map of lengths
        lambda afile: len(                              # return the length of the first string of the tuple
            os.path.splitext(afile)[0]                  # returns first element of tuple 'filename'
        ),
        os.listdir()
    )
)

utils.banner("parse filenames")
#
#   1) filename, extension
#
for file in os.listdir():
    filesplit = os.path.splitext(file)                  # split file in filename, extension
    filename, filext = filesplit                        # assign filename and extension to variables
    print(
        'filename={:<{maxfilenamelen}}, '               # align filename in a field
        'filext={}'.format(                             # print filext
            f'"{filename}"',
            f'"{filext}"',
            maxfilenamelen=maxfilenamelen + 5           # define field witdth
        )
    )

    title, course, number = filename.split('-')         # extract vars from filename
    title = title.strip()                               # remove whitespace
    course = course.strip()                             # remove whitespace
    number = number.strip()[1:].zfill(2)                # remove whitespace and zero pads

    print('title: "{}", course: "{}", number: {}'
          .format(title, course, number))               # print formatted info
    newname = "{}-{}-{}{}".format(                      # recreate filename
        number,
        course,
        title,
        filext
    )
    print(f'file = {file}')
    print(f'newname = {newname}')
    os.rename(file, newname)                            # rename file
    print('.')

utils.banner('final result')
for file in os.listdir():
    print(file)
