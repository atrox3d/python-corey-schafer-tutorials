#
#   https://www.youtube.com/watch?v=ve2pmm5JqmI
#
#################################################################################
import utils
import os


def remove_examplefiles(dirname):
    files = os.listdir(dirname)
    for f in files:
        f = os.path.join(dirname, f)
        isfile = os.path.isfile(f)
        if isfile:
            print(f'deleting {f}')
            os.remove(f)


def create_examplefiles(dirname='multifile', maxfile=10):
    if os.path.exists(dirname):
        remove_examplefiles(dirname)
        os.removedirs(dirname)

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
        print(f'creating : {filepath})')
        with open(filepath, 'w') as file:
            pass
        planetnum += 1
    os.listdir(dirname)


"""
    start
"""
create_examplefiles()
