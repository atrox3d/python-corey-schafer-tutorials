''' JavaScript Object Notation '''
import json

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
print(json_data)
print()

for person in json_data['people']:
    print(f'{person}')
print()

for person in json_data['people']:
    print(f'{person["name"]!r}')
print()

for person in json_data['people']:
    del person['phone']

new_json = json.dumps(json_data, indent=2, sort_keys=True)
print(new_json)
print()


