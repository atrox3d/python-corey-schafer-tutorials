#
#   https://www.youtube.com/watch?v=q5uM4VKywbA
#
#################################################################################
from modules import utils
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
# get file path
csvpath = os.path.join(utils.PROJECT_PATH, 'data', 'names.csv')
print(csvpath)
utils.hashline(char='-')
#
#   open file and list its contents
#
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    print(csvreader)

    # skip firt line of generator
    next(csvreader)

    for line in csvreader:
        print(line)

utils.banner('create new csv from current')
# get new file path
newcsvpath = os.path.join(utils.PROJECT_PATH, 'data', 'newnames.csv')
#
#   open source csv file and read its contents
#
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    #
    #   open dest csv file for writing
    #
    with open(newcsvpath, 'w', newline='') as newcsvfile:
        #
        #   using normal csv writer tab delimited
        #
        csvwriter = csv.writer(newcsvfile, delimiter='\t')
        for line in csvreader:
            csvwriter.writerow(line)
#
#   open new file and list its contents
#
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
#
#   open file and list its contents
#
with open(csvpath, 'r') as csvfile:
    #
    #   using dictreader for input
    #
    dictreader = csv.DictReader(csvfile)

    for line in dictreader:
        print('dictionary line: ', line)
        print('dictionary field: ', line.get('email'))

utils.banner('write csv with dict writer')
#
#   open file and read only the first line to save fields list
#
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fieldnames = next(csvreader)
    print('field names:', fieldnames)
#
#   open source csv file and read its contents
#
with open(csvpath, 'r') as csvfile:
    dictreader = csv.DictReader(csvfile)
    #
    #   open dest csv file for writing
    #
    with open(newcsvpath, 'w', newline='') as newcsvfile:
        #
        #   using dictwriter for output, tab delimited
        #
        dictwriter = csv.DictWriter(newcsvfile, fieldnames, delimiter='\t')
        #
        #   write header fields
        #
        dictwriter.writeheader()

        for line in dictreader:
            dictwriter.writerow(line)

        #
        #   write custom record
        #
        dictwriter.writerow(
            dict(
                first_name="my",
                last_name="custom",
                email="record",
            )
        )

utils.banner('read new csv with dict reader')
#
#   open dest csv file and list its contents
#
with open(newcsvpath, 'r') as newcsvfile:
    dictreader = csv.DictReader(newcsvfile, delimiter='\t')

    for line in dictreader:
        print('dictionary line: ', line)
        print('dictionary field: ', line.get('email'))
