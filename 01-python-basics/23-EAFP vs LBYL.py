#
#   https://www.youtube.com/watch?v=x3v9zMX1s4s
#
#   Python Tutorial: Duck Typing and Asking Forgiveness, Not Permission (EAFP)
#
#################################################################################
from modules import utils

person1 = dict(
    name='jess',
    age=23,
    job='programmer'
)

person2 = dict(
    name='jess',
    age=23,
)


def printpersonLBYL(p):
    if 'name' in p and 'age' in p and 'job' in p:
        print("i'm {name}. i'm {age} and i am a {job}".format(**p))
    else:
        print('missing some keys')


def printpersonEAFP(p):
    try:
        print("i'm {name}. i'm {age} and i am a {job}".format(**p))
    except KeyError as ke:
        print('missing {} key'.format(ke))


########################################################################################################################
#
# print person LBYL
#
########################################################################################################################
utils.banner('print person LBYL')
printpersonLBYL(person1)
printpersonLBYL(person2)
########################################################################################################################
#
# print person EAFP
#
########################################################################################################################
utils.banner('print person EAFP')
printpersonEAFP(person1)
printpersonEAFP(person2)


########################################################################################################################
def printlistLBYL(l):
    if len(l) >= 6:
        print(l[5])
    else:
        print('that index does not exist')


def printlistEAFP(l):
    try:
        print(l[5])
    except IndexError as ie:
        print(ie)


mylist = list(range(1, 6))

idx = 0
print(len(mylist))
print(mylist)
for i in mylist:
    print(idx, i)
    idx += 1

printlistLBYL(mylist)
printlistEAFP(mylist)
