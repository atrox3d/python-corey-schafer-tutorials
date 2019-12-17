#
#   https://www.youtube.com/watch?v=ve2pmm5JqmI
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
    utils.banner('DELETE EXISTING EXAMPLE FILES')
    files = os.listdir(dirname)
    for f in files:
        f = os.path.join(dirname, f)
        if os.path.isfile(f):
            print(f'deleting {f}')
            os.remove(f)


def create_examplefiles(dirname):
    """
    create example files
    :param dirname:
    :param maxfile:
    :return:
    """
    if os.path.exists(dirname):
        remove_examplefiles(dirname)
        os.removedirs(dirname)

    utils.banner('CREATE EXAMPLE FILES')
    os.makedirs(dirname)
    # create random ordered list
    planets = {
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
        filename = f'{planet} - our solar system - #{planetnum}.mp4'
        filepath = os.path.join(dirname, filename)
        print(f'creating : {filepath}')
        with open(filepath, 'w') as file:
            pass
        planetnum += 1
    os.listdir(dirname)


"""

    start by creating the files
    
"""
exampledir = 'multifile'
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
maxtuplelen = max(
    # returns a map of lengths
    map(
        # return the length of the string representation of the tuple
        lambda afile: len(str(os.path.splitext(afile))),
        os.listdir()
    )
)
#
#   get max length of first string of tuples
#
maxfilenamelen = max(
    # returns a map of lengths
    map(
        # return the length of the first string of the tuple
        lambda afile: len(os.path.splitext(afile)[0]),
        os.listdir()
    )
)

utils.banner("parse filenames")
#
#   1) filename, extension
#
for file in os.listdir():
    #
    #   split file in filename, extension
    #
    filesplit = os.path.splitext(file)
    #
    #   assign filename and extension to variables
    #
    filename, filext = filesplit
    #print(f'{str(filesplit):<{maxtuplelen + 5}} -> {filename:<{maxfilenamelen + 5}} {filext}')
    #print(f'filename: {filename:<{maxfilenamelen + 5}}, filext: {filext}')

    # name, ext = [x for x in file.values()]
    print(
            'filename={:<{maxfilenamelen}}, filext={}'.format(
                                                            f'"{filename}"',
                                                            f'"{filext}"',
                                                            maxfilenamelen=maxfilenamelen+5
                                                )
    )

    title, course, number = filename.split('-')

    title = title.strip()
    course = course.strip()
    number = number.strip()[1:].zfill(2)

    print('title: "{}", course: "{}", number: {}'.format(title, course, number))
    newname = "{}-{}-{}{}".format(number, course, title, filext)
    print(f'file = {file}')
    print(f'newname = {newname}')
    os.rename(file, newname)
    print('.')

utils.banner('final result')
for file in os.listdir():
    print(file)


