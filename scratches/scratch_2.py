def x(**kwargs):
    fstrings = []
    for k, v in kwargs.items():
        fstrings.append(f'{k} = {v}')
        # print(fstrings)
    print(", ".join(fstrings))


a = 1
c = 9
x(a=a, c=c)


def reset(*othersymbols):
    """
    deletes the predefined globasl a, b, and c, if they exist
    and deletes oprtionally any other symbol passed as argument [ string, ... ]
    """

    # predefined variables
    symbols = [
        'a',
        'b',
        'c',
    ]

    # add any optional variables
    symbols.extend(othersymbols)

    # seek and destroy
    for symbol in symbols:
        if symbol in globals():
            print(f'deleting {symbol}')
            del globals()[symbol]


def resetglobals(debug=False):
    for g in list(globals()):
        if g.startswith('__'):
            if debug: print(f'skipping {g}')
            continue
        if g.endswith("globals"):
            if debug: print(f'skipping {g}')
            continue
        print(f'deleting {g}')
        del globals()[g]

    del g


def printglobals(debug=False):
    fstrings = []
    for k, v in globals().items():
        if k.startswith('__'):
            if debug: print(f'skipping {k}')
            continue
        t = globals()[k].__class__.__name__
        if debug: print(f'"{t}"')
        if t == 'function':
            if debug: print(f'skipping {k}')
            continue
        fstrings.append(f'{k} = {v}')
    print(", ".join(fstrings))
