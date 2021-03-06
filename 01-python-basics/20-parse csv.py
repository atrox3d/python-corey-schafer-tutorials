#
#   https://www.youtube.com/watch?v=bkpLhQd6YQM
#
#   Python Tutorial: Real World Example - Parsing Names From a CSV to an HTML List
#
#################################################################################
import csv
import os
from modules import utils

html = ''
names = []
cwd = os.getcwd()
filepath = os.path.join(utils.PROJECT_PATH, 'data', 'patrons.csv')

print(f'data file: {filepath}')
if not os.path.exists(filepath):
    print(f'data file "{filepath}" missing\nexiting')
    exit(1)

with open(filepath, 'r') as datafile:
    csvdata = csv.DictReader(datafile)

    # header line is consumed by the dictreader as keys
    # next(csvdata)
    # we dont want header or first line of bad data
    next(csvdata)

    for line in csvdata:
        if line['FirstName'].lower() == "no reward":
            break
        names.append(f'{line["FirstName"]} {line["LastName"]}')

html += f'<p>current number of contributors : {len(names)}<p>'
html += '\n<ul>'

for name in names:
    html += f'\n\t<li>{name}</li>'

html += '\n</ul>'

print(html)
