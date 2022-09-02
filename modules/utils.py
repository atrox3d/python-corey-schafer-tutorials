"""


little utilities library


"""
import os


def hashline(width=120, char='#'):
    """
    prints a separation line on terminal

    :param width:   optional jwidth of the separation line.
                    defaults to 160
    :param char:    optional character to repeat.
                    defaults to hash '#'
    :return:        nothing
        :rtype: None
    """
    print(char * width)


def dashline(width=120):
    hashline(char='-')


def banner(*lines, height=3, width=120, char='#'):
    """
    prints a separation banner on terminal

    :param text:    text to print inside the banner
    :param height:  optional height of the banner
                    defaults to 3
    :param width:   optional width of the hashline
                    defaults to 160
    :param char:    optional character to repeat into the hashline
                    defaults to hash
    :return:        nothing
        :rtype: None
    """
    #
    #   first hashline
    #
    hashline(width, char)
    spacing = height // 2 + 1
    #
    #   upper single hashtags
    #
    for spaceline in range(1, spacing):
        print(char)
    #
    #   prints the message
    #
    # print(type(lines))
    # print(len(lines))
    for line in lines:
        sublines = line.split('\n')
        for subline in sublines:
            print(f'{char} {subline}')
    #
    #   lower single hashtags
    #
    for spaceline in range(1, spacing):
        print(char)
    #
    #   last hashline
    #
    hashline(width, char)


def get_dict_from_obj(obj):
    """
    creates a dictionary from an object.
    useful wher vars(obj) fails due to missing .__dict__

    :param obj: object to get attributes from
    :return:
        :rtype: dict
    """
    return {name: getattr(obj, name) for name in dir(obj) if not name.startswith('__')}.items()


def print_object_details(obj, name, properties=True, innerclasses=True, functions=True):
    """
    prints detailed info about the members of an object

    :param obj:             the object to examine
    :param name:            name of the object variable to print
    :param properties:      switch to enable properties printing
    :param innerclasses:    switch to enable innerclasses printing
    :param functions:       switch to enable methods printing
    :return:    Nothing
        :rtype: None
    """
    items = get_dict_from_obj(obj)

    if properties:
        banner(f'properties of {name}')
        for k, v in items:
            if isinstance(v, int):
                print(f'{k:<20}|{str(type(v)):<20}:{v:>10}')

    if innerclasses:
        banner(f'inner classes of {name}')
        for k, v in items:
            if "function" in str(type(v)):
                print(f'{k:<20}|{str(type(v))}')

    if functions:
        banner(f'functions of {name}')
        if "function" not in str(type(v)) and not isinstance(v, int):
            print(f'{k:<20}|{str(type(v)):<20}')


MAXLEN = 30


def printfvar(var, varname=None, maxlen=MAXLEN):
    """
    prints varname, var type and value formatted
    :param maxlen:
    :param varname:
    :param var:
    :return:
    """
    if varname is None:
        varname = getattr(var, '__name__', f'{{{var.__class__.__name__}}}')

    varname = f'{varname}'
    vartype = f'{str(type(var))}'
    # print(f'{varname:<20} type: {vartype:<30} value: {var if not var is None else "none"}')
    print(f'{"varname: " + varname:>{MAXLEN}.{MAXLEN}} | {"type: " + vartype:<30} | value: {repr(var)}')


def getprojectpath(subfolder=None):
    debug = False
    module_path = __file__
    module_dir = os.path.dirname(__file__)
    project_dir_rel = os.path.join(module_dir, '..')
    project_dir_abs = os.path.abspath(project_dir_rel)

    if debug:
        print(project_dir_rel)
        print(project_dir_abs)

    if subfolder is not None:
        return os.path.join(project_dir_abs, subfolder)
    return project_dir_abs


PROJECT_PATH = getprojectpath()
PROJECTDATA_PATH = getprojectpath('data')
PROJECTMODULES_PATH = getprojectpath('modules')


def getdatafilepath(filename):
    filepath = os.path.join(PROJECTDATA_PATH, os.path.basename(filename))
    return filepath


if __name__ == "__main__":
    banner("hello")
    banner("hello", "there")
    banner("hello", "there", char='*', height=10, width=20)
    banner("hello", "there", char='*')
    banner("hello", "there", char='*', height=10)

    print('PROJECT_PATH:', PROJECT_PATH)
    print('PROJECTDATA_PATH:', PROJECTDATA_PATH)
    print('PROJECTMODULES_PATH:', PROJECTMODULES_PATH)

