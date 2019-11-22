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

    lplanets = list(planets)

    for num in range(0, len(lplanets)):
        planet = lplanets[num]
        filename = f'{planet} - our solar system - # {num}.mp4'
        filepath = os.path.join(dirname, filename)
        print(f'creating : {filepath})')
        with open(filepath, 'w') as file:
            pass

    os.listdir(dirname)


create_examplefiles()
