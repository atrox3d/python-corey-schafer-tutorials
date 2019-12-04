#
#   https://www.youtube.com/watch?v=K8L6KVGG-7o
#
#################################################################################
import utils
import re
from collections import namedtuple
import os


def printfvar(varname, var):
    varname = f'{varname},'
    vartype = f'{str(type(var))},'
    print(f'{varname:<20} type: {vartype:<30} value: {var if not var is None else "none"}')


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#
#   3 groups:
#       - optional www
#       - domain name
#       - top level domain
#
topleveldomain = r'https?://(www\.)?(\w+)(\.\w+)'
pattern = re.compile(topleveldomain)
###############################################################################################
#
#
#   find groups
#
#
###############################################################################################
utils.banner('find groups')
finditer = pattern.finditer(urls)

printfvar('finditer', finditer)
#
# loop over finditer
#
for match in finditer:
    printfvar('match', match)
    #
    #   loop over groups inside every match
    #
    groups = []
    printfvar('match.groups', match.groups())
    for group in match.groups():
        printfvar('group', group)
        #
        # format every group
        #
        group = "" if group is None else group
        groups.append(f'{group:<10}')
    #
    #   add the entire match : group 0
    #
    line = f'{match.group(0):<25}, '
    #
    #   join formatted groups
    #
    line += ", ".join(groups)
    print(line)
###############################################################################################
#
#
#   replace groups
#
#
###############################################################################################
utils.banner(r'replace groups: replace each url with \2\3')

subbedurls = pattern.sub(r'\2\3', urls)
printfvar('subbedurls', subbedurls)

###############################################################################################
#
#
#   findall
#
#
###############################################################################################
utils.banner(r'findall')

findall = pattern.findall(urls)
printfvar('findall', findall)
for found in findall:
    printfvar('found', found)
