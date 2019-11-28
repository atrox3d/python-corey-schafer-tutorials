#
#   https://www.youtube.com/watch?v=bkpLhQd6YQM
#
#################################################################################
import utils
import csv
import os

html = ''
names = []
cwd = os.getcwd()
filepath = os.path.join(cwd, 'data', 'patrons.csv')

print(f'data file: {filepath}, {"ok" if os.path.exists(filepath) else "doesnt exist"}')

