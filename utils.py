"""


little utilities library


"""


def hashline(width=160, char='#'):
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


def banner(text, height=3, width=160, char='#'):
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
    hashline(width, char)
    spacing = height // 2 + 1
    for spaceline in range(1, spacing):
        print(char)
    print(f'{char} {text}')
    for spaceline in range(1, spacing):
        print(char)
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

