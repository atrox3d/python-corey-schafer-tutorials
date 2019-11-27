#
#   https://www.youtube.com/watch?v=q5uM4VKywbA
#
#################################################################################
import utils
import csv
import os

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



