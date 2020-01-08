''' JavaScript Object Notation '''

import json
from modules import utils

#######################################################################################################
utils.banner(
                'load and display states.json names and abbreviations'
)
#######################################################################################################
with open(utils.getdatafilepath('states.json')) as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])
#######################################################################################################
utils.banner(
                'delete area_codes, save to new_states.json, load and display prettified'
)
#######################################################################################################
for state in data['states']:
    del state['area_codes']

with open(utils.getdatafilepath('new_states.json'), 'w') as f:
    json.dump(data, f, indent=2)

with open(utils.getdatafilepath('new_states.json')) as f:
    data = json.load(f)
    print(json.dumps(data, indent=2))
