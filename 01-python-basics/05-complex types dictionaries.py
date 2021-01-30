#
# https://www.youtube.com/watch?v=daefaLgNkw0
#
# Python Tutorial for Beginners 5: Dictionaries - Working with Key-Value Pairs
#
#################################################################################
#
#   create student dictionary
#
student = {'name': 'robb', 'age': 25, 'courses': ['math', 'compsci'], 1: 'one'}
print("student: ", student)
        # student:  {'name': 'robb', 'age': 25, 'courses': ['math', 'compsci'], 1: 'one'}
#
#   print single dict fields
#
print(f'student.name    : {student["name"]}')                       # student.name    : robb
print(f'student.age     : {student["age"]}')                        # student.age     : 25
print(f'student.courses : {student["courses"]}')                    # student.courses : ['math', 'compsci']
print(f'student.1       : {student[1]}')                            # student.1       : one
#
# non existent key with exception
#
try:
    print(f'student.phone   : {student["phone"]}')
except KeyError as ke:
    print('key not found', ke)                                      # key not found 'phone'
#
# non existent key with default
#
print(f'student.phone   : {student.get("phone", "not found")}')     # student.phone   : not found
#
# existent key with default
#
student['phone'] = '555-555'
print(f'student.phone   : {student.get("phone", "not found")}')     # student.phone   : 555-555
#
# update multiple keys
#
student.update({'name': 'mark', 'age': 47, 'newkey': 'newval'})
print("student: ", student)
        # student:  {'name': 'mark', 'age': 47, 'courses': ['math', 'compsci'], 1: 'one', 'phone': '555-555', 'newkey': 'newval'}
#
# key deletion
#
del student['age']
print("student: ", student)
        # student:  {'name': 'mark', 'courses': ['math', 'compsci'], 1: 'one', 'phone': '555-555', 'newkey': 'newval'}
#
#   remove and return value
#
phone = student.pop('phone')
print(f'phone: {phone}, student: {student}')
    # phone: 555-555, student: {'name': 'mark', 'courses': ['math', 'compsci'], 1: 'one', 'newkey': 'newval'}
print(f'student length: {len(student)}')                # 4
print(f'student keys: {student.keys()}')                # student keys: dict_keys(['name', 'courses', 1, 'newkey'])
print(f'student values: {student.values()}')            # student values: dict_values(['mark', ['math', 'compsci'], 'one', 'newval'])
print(f'student items: {student.items()}')
        # student items: dict_items([('name', 'mark'), ('courses', ['math', 'compsci']), (1, 'one'), ('newkey', 'newval')])
#
#   iteration
#
for key in student:
    print(f'{key}: {student[key]}')
    print(f'{key}: {student.get(key)}')
            # name: mark
            # name: mark
            # courses: ['math', 'compsci']
            # courses: ['math', 'compsci']
            # 1: one
            # 1: one
            # newkey: newval
            # newkey: newval


for key, val in student.items():
    print(f'{key}: {val}')
            # name: mark
            # courses: ['math', 'compsci']
            # 1: one
            # newkey: newval
