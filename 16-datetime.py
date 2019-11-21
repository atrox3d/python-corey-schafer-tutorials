#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################


def hashline(width=160, char='#'):
    print(char * width)


def banner(text, height=3, width=160, char='#'):
    hashline(width, char)
    spacing = height // 2 + 1
    for spaceline in range(1, spacing):
        print(char)
    print(f'{char} {text}')
    for spaceline in range(1, spacing):
        print(char)
    hashline(width, char)


import datetime

"""

NAIVE date times


"""
banner("NAIVE date times")
d = datetime.datetime(2019, 11, 20)
print(d)

today = datetime.date.today()
print(today)

items = {name: getattr(today, name) for name in dir(today) if not name.startswith('__')}.items()

banner('integer properties of today')
for k, v in items:
    if isinstance(v, int):
        print(f'{k:<20}|{str(type(v)):<20}:{v:>10}')

banner('methods of today')
for k, v in items:
    if "function" in str(type(v)):
        print(f'{k:<20}|{str(type(v))}')

banner('inner classes of today')
for k, v in items:
    if "function" not in str(type(v)) and not isinstance(v, int):
        print(f'{k:<20}|{str(type(v)):<20}')

banner('today functions')
print(f'weekday     : {today.weekday()}')
print(f'iso weekday : {today.isoweekday()}')

banner('time deltas')
delta = datetime.timedelta(days=7)
print(f'today          : {today}')
print(f'today + 7 days : {today + delta}')
print(f'today - 7 days : {today - delta}')

bday = datetime.date(2020, 7, 13)
till_bday = bday - today
print(f'\ndays until my birthday : {till_bday}')
items = {name: getattr(till_bday, name) for name in dir(till_bday) if not name.startswith('__')}.items()

banner('integer properties of timedelta')
for k, v in items:
    if isinstance(v, int):
        print(f'{k:<20}|{str(type(v)):<20}:{v:>10}')

banner('methods of timedelta')
for k, v in items:
    if "function" in str(type(v)):
        print(f'{k:<20}|{str(type(v))}')

banner('inner classes of today')
for k, v in items:
    if "function" not in str(type(v)) and not isinstance(v, int):
        print(f'{k:<20}|{str(type(v)):<20}')

banner('timedelta functions')
print(f'weekday     : {today.weekday()}')
print(f'iso weekday : {today.isoweekday()}')

