#
#   https://www.youtube.com/watch?v=q5uM4VKywbA
#
#################################################################################
import utils
import csv
import os

#################################################################################
#
#
#
#   STANDARD CSV READER
#
#
#
#################################################################################
utils.banner('open data/names.csv and list its content')
csvpath = os.path.join(os.getcwd(), 'data', 'names.csv')
print(csvpath)
utils.hashline(char='-')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    print(csvreader)
    # skip firt line of generator
    next(csvreader)

    for line in csvreader:
        print(line)

utils.banner('create new csv from current')
newcsvpath = os.path.join(os.getcwd(), 'data', 'newnames.csv')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    with open(newcsvpath, 'w', newline='') as newcsvfile:
        csvwriter = csv.writer(newcsvfile, delimiter='\t')
        for line in csvreader:
            csvwriter.writerow(line)

with open(newcsvpath, 'r') as newcsvfile:
    newcsvreader = csv.reader(newcsvfile, delimiter='\t')
    for line in newcsvreader:
        print(line)

#################################################################################
#
#
#
#   DICTIONARY CSV READER
#
#
#
#################################################################################
utils.banner('read csv with dict reader')
with open(csvpath, 'r') as csvfile:
    dictreader = csv.DictReader(csvfile)

    for line in dictreader:
        print('dictionary line: ', line)
        print('dictionary field: ', line.get('email'))

utils.banner('write csv with dict writer')
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldnames = next(csvreader)
    print('field names:', fieldnames)

with open(csvpath, 'r') as csvfile:
    dictreader = csv.DictReader(csvfile)

    with open(newcsvpath, 'w', newline='') as newcsvfile:
        dictwriter = csv.DictWriter(newcsvfile, fieldnames, delimiter='\t')
        for line in dictreader:
            dictwriter.writerow(line)

utils.banner('read new csv with dict reader')
with open(newcsvpath, 'r') as newcsvfile:
    dictreader = csv.DictReader(newcsvfile)

    for line in dictreader:
        print('dictionary line: ', line)
        print('dictionary field: ', line.get('email'))
