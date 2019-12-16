##############################################################################################
#
#
#   FUNCTIONS
#
#
##############################################################################################
def myfunc(*args):
    print('args type: ', type(args))
    count = 0
    for arg in args:
        print(f'param #{count} : {arg}')


# pass a variable number of arguments
myfunc(1, 2, 3, 4, [5, 6, 7])
# pass a variable number of arguments AND unpack a list
myfunc(1, 2, 3, 4, *[5, 6, 7])
# pass a variable number of arguments AND unpack a list AND a dict key
myfunc(1, 2, 3, 4, *{'x': 10})


def myfunc(**kwargs):
    print('kwargs type: ', type(kwargs))
    for k, v in kwargs.items():
        print(f'{k}={v}')


# pass a variable number of named arguments
myfunc(a=1, b=2, c=3)
# pass a variable number of named arguments AND unpack a dictonary
myfunc(a=1, b=2, c=3, **{'d': 4, 'e': 5})


def args_order(std, args, first, *thenvariableargs, **andthenkeywordarguments):
    print(f'std   = {std}')
    print(f'args  = {args}')
    print(f'first = {first}')

    count = 0
    for arg in thenvariableargs:
        print(f'thenvariableargs[{count}] = {arg}')

    for kwname, kwvalue in andthenkeywordarguments.items():
        print(f'{kwname} = {kwvalue}')


args_order('std', 'args', 'first')
args_order('std', 'args', 'first', 1, 2, 3, 4, 5)
args_order('std', 'args', 'first', 1, 2, 3, 4, 5, a=1, b=2, **dict(c=3, d=4, e=5), **{'f':6})
args_order('std', 'args', 'first', a=1, b=2, **dict(c=3, d=4, e=5), **{'f':6})

dict1={
    'c':3,
    'd':4,
    'e':5,
}
dict2 = dict(
    f=6
)
args_order('std', 'args', 'first', a=1, b=2, **dict1, **dict2)

# NOPE
# args_order(a=1, b=2, **dict(c=3, d=4, e=5), **{'f':6})

###########################
# keyword only
##########################
# NOPE
# def keywordonly(*, **kwargs):
# def keywordonly(*, *kwargs):
def keywordonly(*, keyword, default=True, anotherkw):
    print("keyword ={}, default={}, anotherkw={}".format(keyword, default, anotherkw))
    print("keyword ={0}, default={1}, anotherkw={2}".format(keyword, default, anotherkw))
    print(f"keyword ={keyword}, default={default}, anotherkw={anotherkw}")

# NOPE
# keywordonly()
# NOPE
# keywordonly(keyword='keyword')
keywordonly(keyword='keyword', default=False, anotherkw='anotherkw')
keywordonly(keyword='keyword', anotherkw='anotherkw')
keywordonly(**dict(keyword='keyword', anotherkw='anotherkw'))
dictx=dict(
    keyword='keyword',
    anotherkw='anotherkw'
)
keywordonly(**dictx)


exit()


##############################################################################################
#
#
#   LISTS
#
#
##############################################################################################
my_list = [1, 2, 3]
print(my_list)

# unpack list elements to arguments
print(*my_list)


###########################################
# NOPE
# for x in *my_list:
#     print(x)
###########################################

###########################################
# NOPE
# a, b, c = *my_list
###########################################

###########################################
# NOPE
# (a,b,c) = *my_list
###########################################

###########################################
# YEP
###########################################
def myfn(a, b, c):
    print(a, b, c)


myfn(*my_list)

###########################################
# NOPE
# def myfn(a, b, c, d):
#     print(a, b, c, d)
#
# myfn(*my_list)
###########################################

###########################################
# YEP
###########################################
my_list = list(range(0, 10))
print(my_list)

# assign different parts of a list to multiple variables
a, *blist, c = my_list
print(f'a={a}, b={blist}, c={c}')
a, b, *clist, d, e, f = my_list
print(f'a={a}, b={b}, c={clist}, d={d}, e={e}, f={f}')

###########################################
# YEP
###########################################
list1 = list(range(0, 10))
list2 = list(range(10, 20))
merge = [*list1, *list2]
print(f'list1 = {list1}')
print(f'list2 = {list2}')
print(f'merge = {merge}')
##############################################################################################
#
#
#   DICTIONARIES
#
#
##############################################################################################

dict1 = {
    'a': 1,
    'b': 2,
}

dict2 = {
    'c': 3,
    'd': 4,
}

# merge keys
kmerge = {*dict1, *dict2}
print(kmerge)

# merge dictionaries
dmerge = {**dict1, **dict2}
print(dmerge)
##############################################################################################
#
#
#   STRINGS
#
#
##############################################################################################

# unpack string to list
string = "hello, world"
lstring = [*string]
print(lstring)

# unpack string to multiple variables
a, *b, c = string
print(a, b, c)
