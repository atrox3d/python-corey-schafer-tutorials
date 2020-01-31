import sys


def listpackagepaths():
    print('-' * 80)
    for p in sys.path:
        if 'importing' in p or '..' in p:
            print(p)
    print('-' * 80)


PYCHARM_MARKASSOURCE_PARENT = False
SIBLING_IMPORT = True


listpackagepaths()


if PYCHARM_MARKASSOURCE_PARENT:
    #
    #   pycharm adds .. to sys.path
    #
    #   importing
    #   importing\\pizza_app\\pizza_shop
    print('pycharm mark as sources root')
    from pizza_app_experiments.pizzapy import menu
elif SIBLING_IMPORT:
    #
    #   trick for siblings import
    #
    #   importing'
    #   importing\\pizza_app\\pizza_shop
    print('sibling import')
    sys.path.append('..')
    listpackagepaths()
    from pizzapy import menu
else:
    #
    #   use relative import
    #
    #   importing\\pizza_app\\pizza_shop
    print('relative import')
    sys.path.append('../..')
    listpackagepaths()
    from pizza_app_experiments.pizzapy import menu

print(menu.MENU)

