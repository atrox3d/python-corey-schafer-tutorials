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

utils.banner(f'changing to {exampledir} directory and listing contents')
print('current directory: ', os.getcwd())
os.chdir(os.path.join(os.getcwd(), exampledir))
print('current directory: ', os.getcwd())

utils.hashline(char='-')
for filename in os.listdir():
    print(filename)
utils.hashline(char='-')


