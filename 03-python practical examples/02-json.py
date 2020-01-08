''' JavaScript Object Notation '''

import json
from modules import utils

people_string = '''
{
    "people": [
        {
            "name": "john smith",
            "phone": "615-555-7164",
            "emails": [
                "johnsmith@bogusemail.com",
                "john.smith@work-place.com"
            ],
            "has_license": false
        },
        {
            "name": "jane doe",
            "phone": "560-555-5153",
            "emails": null,
            "has_license": true
        }
    ]
}
'''

json_data = json.loads(people_string)

utils.banner('json_data raw dump')
print(json_data)
print()

utils.banner('json_data print each person')
for person in json_data['people']:
    print(f'{person}')
print()

utils.banner('json_data print each person name')
for person in json_data['people']:
    print(f'{person["name"]!r}')
print()

utils.banner('json_data delete each person phone and dump prettified')
for person in json_data['people']:
    del person['phone']

new_json = json.dumps(json_data, indent=2, sort_keys=True)
print(new_json)
print()


