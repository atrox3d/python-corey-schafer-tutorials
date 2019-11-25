#
#   https://www.youtube.com/watch?v=ve2pmm5JqmI
#
#################################################################################
import utils
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
        filename = f'{planet} - our solar system - # {planetnum}.mp4'
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
utils.hashline(char='-')
#
#   start parsing the filenames
#
##########################################################################################################
#
#   apply os.path.splitext to each file in current directory
#   return a map
#
splitmap = map(os.path.splitext, os.listdir())
print('splitmap: ', splitmap)
#
#   cast map to list
#
splitmaplist = list(splitmap)
print('splitmaplist: ', splitmaplist)
#
#   generator of list of splitted filenames
#
splitgen = (f for f, e in splitmaplist)
print('splitgen', splitgen)
#
#   cast generator to list
#
splitgenlist = list(splitgen)
print('splitgenlist', splitgenlist)
#
#   find longest string in splitgenlist and calculate length
#
longest = max(splitgenlist, key=len)
width = len(longest) + 20
print(longest, width)

for file in os.listdir():
    filesplit = os.path.splitext(file)
    filename, filext = filesplit
    print(f'{str(filesplit):<{width}} -> {filename}, {filext}')
