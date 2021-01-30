#
# https://www.youtube.com/watch?v=W8KRzm-HUcc
#
# Python Tutorial for Beginners 4: Lists, Tuples, and Sets
#
#################################################################################
#
# empty lists
#
el = []
el = list()
#
# empty tuples
#
et = ()
et = tuple()
#
# empty dictionaries
#
ed = {}
ed = dict()
#
# empty sets
#
es = {}  # no, this is an empty dictionary
es = set()
#
# empty generators
#
eg = (x for x in [])
#
# memo
#
##############################################################################
#
#   empty dictionary to hold example types and description
#
type_empties = {}
#
#   empty list
#
type_empties[type(el)] = el
#
#   empty tuple
#
type_empties[type(et)] = et
#
#   empty dictionary
#
type_empties[type(ed)] = ed
#
#   empty set
#
type_empties[type(es)] = es
#
#   empty generator
#
type_empties[type(eg)] = eg
#
#   display dictionary
#
for typeclass, typeempty in type_empties.items():
    #
    # extract class name
    #
    typename = typeclass.__name__
    print(f'{typename:<10}: {typeempty}')
