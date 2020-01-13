#
#   https://youtu.be/sugvnHA7ElY
#
#################################################################################
from modules import utils
import os


def main():
    utils.banner(
        'https://youtu.be/sugvnHA7ElY',
        "if __name__ == '__main__'"
    )
    print(f'{os.path.basename(__file__)}\'s name: "{__name__}"')


if __name__ == '__main__':
    main()
