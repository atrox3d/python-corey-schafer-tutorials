#
# https://www.youtube.com/watch?v=daefaLgNkw0
#
#################################################################################
#
#   create student dictionary
#
student = {'name': 'robb', 'age': 25, 'courses': ['math', 'compsci'], 1: 'one'}
print("student: ", student)
#
#   print single dict fields
#
print(f'student.name    : {student["name"]}')
print(f'student.age     : {student["age"]}')
print(f'student.courses : {student["courses"]}')
print(f'student.1       : {student[1]}')
#
# non existent key with exception
#
try:
    print(f'student.phone   : {student["phone"]}')
except KeyError as ke:
    print('key not found', ke)
#
# non existent key with default
#
print(f'student.phone   : {student.get("phone", "not found")}')
#
# existent key with default
#
student['phone'] = '555-555'
print(f'student.phone   : {student.get("phone", "not found")}')
#
# update multiple keys
#
student.update({'name': 'mark', 'age': 47, 'newkey': 'newval'})
print("student: ", student)
#
# key deletion
#
del student['age']
print("student: ", student)
#
#   remove and return value
#
phone = student.pop('phone')
print(f'phone: {phone}, student: {student}')
print(f'student length: {len(student)}')
print(f'student keys: {student.keys()}')
print(f'student values: {student.values()}')
print(f'student items: {student.items()}')
#
#   iteration
#
for key in student:
    print(f'{key}: {student[key]}')
    print(f'{key}: {student.get(key)}')

for key, val in student.items():
    print(f'{key}: {val}')
