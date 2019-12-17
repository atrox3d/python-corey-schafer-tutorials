#
#   https://www.youtube.com/watch?v=eirjjyP2qcQ
#
#################################################################################
import datetime


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


def get_dict_from_obj(obj):
    return {name: getattr(obj, name) for name in dir(obj) if not name.startswith('__')}.items()


def print_object_details(obj, name, properties=True, innerclasses=True, functions=True):
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


"""

NAIVE date times


"""
banner("NAIVE date times")
d = datetime.datetime(2019, 11, 20)
print(d)
#
#
#   datetime.date
#
#
today = datetime.date.today()
print(today)
print_object_details(today, 'today')

banner('today functions')
print(f'weekday     : {today.weekday()}')
print(f'iso weekday : {today.isoweekday()}')
#
#
#   datetime.timedelta
#
#
banner('time deltas')
delta = datetime.timedelta(days=7)
print(f'today          : {today}')
print(f'today + 7 days : {today + delta}')
print(f'today - 7 days : {today - delta}')

bday = datetime.date(2020, 7, 13)
till_bday = bday - today
print(f'\ndays until my birthday : {till_bday}')
print_object_details(till_bday, 'timedelta')

banner('timedelta functions')
print(f'weekday     : {today.weekday()}')
print(f'iso weekday : {today.isoweekday()}')
#
#
#   datetime.time
#
#
banner('time')
t = datetime.time(9, 30, 45, 100000)
print(f'time : {t}')
print_object_details(t, 'time')
#
#
#   datetime.datetime
#
#
dt = datetime.datetime(2019, 11, 21, 10, 15, 30, 100000)
print('datetime.datetime(2019, 11, 21, 10, 15, 30, 100000) : ', dt)
dt_today = datetime.datetime.today()
print('datetime.datetime.today()                           : ', dt_today)
dt_now = datetime.datetime.now()
print('datetime.datetime.now()                             : ', dt_now)
dt_utcnow = datetime.datetime.utcnow()
print('datetime.datetime.utcnow()                          : ', dt_utcnow)
#
#   strftime, strptime
#
banner('strftime, strptime')
datetimeformat = "%d/%m/%Y %H:%M"
# 22/11/2019 10:45
datetimeobj = datetime.datetime.today()
fwidth = 30
print(f'{"datetimeobj":<{fwidth}}: {datetimeobj}')
datetostring = datetimeobj.strftime(datetimeformat)
print(f'{"datetostring":<{fwidth}}: {datetostring}')
# stringtodate = datetime.datetime.strptime("22/11/2019 10:45", datetimeformat)
stringtodate = datetime.datetime.strptime(datetostring, datetimeformat)
print(f'{"stringtodate":<{fwidth}}: {stringtodate}')
stringtodate_fmt = stringtodate.strftime(datetimeformat)
print(f'{"stringtodate formatted":<{fwidth}}: {stringtodate_fmt}')




