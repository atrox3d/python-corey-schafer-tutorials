#
# https://www.youtube.com/watch?v=D3JvDWO-BY4
#
#################################################################################


def print_sortedobj(banner_title, original_obj, sorted_obj):
    print("#" * 80)
    print(banner_title)
    print("#" * 80)
    print(f'original <{original_obj.__class__.__name__}> : {original_obj}')
    print(f'sorted() <{sorted_obj.__class__.__name__}> : {sorted_obj}')
    print('----> sorted() always returns a list')
    print()


"""


tuples


"""
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
try:
    tup.sort()
except AttributeError as ae:
    print(f'cannot call .sort on a {tup.__class__.__name__} : ', ae)

sorted_tuple = sorted(tup)
print_sortedobj("sorted tuple", tup, sorted_tuple)

"""


dictionaries


"""
di = {
    'name': 'robb',
    'job': 'programmer',
    'age': None,
    'os': 'winshit'
}

try:
    di.sort()
except AttributeError as ae:
    print(f'cannot call .sort of a {di.__class__.__name__} : ', ae)

sorted_di = sorted(di)
print_sortedobj("sorted dict", di, sorted_di)
"""


user defined classes


"""


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('carl', 37, 70000)
e2 = Employee('sarah', 29, 80000)
e3 = Employee('john', 43, 90000)

employees = [e1, e2, e3]
#
#   python does not know how to order employee class
#
try:
    sorted_employees = sorted(employees)
except TypeError as te:
    print('cannot sort class :', te)


#
#   define a key function to use with sorted()
#
def employee_sortkey(employee):
    return employee.name


sorted_employees = sorted(employees, key=employee_sortkey)
print_sortedobj('sort class employee by name', employees, sorted_employees)


#
#   define a key function to use with sorted()
#
def employee_sortkey(employee):
    return employee.age


sorted_employees = sorted(employees, key=employee_sortkey)
print_sortedobj('sort class employee by age', employees, sorted_employees)


#
#   define a key function to use with sorted()
#
def employee_sortkey(employee):
    return employee.salary


sorted_employees = sorted(employees, key=employee_sortkey, reverse=True)
print_sortedobj('sort class employee by salary, reversed', employees, sorted_employees)
#
# using lambdas
#
sorted_employees = sorted(employees, key=lambda emp: emp.age, reverse=True)
print_sortedobj('sort class employee by age, reversed, using lambda', employees, sorted_employees)
#
# using attrgetter
#
from operator import attrgetter

sorted_employees = sorted(employees, key=attrgetter('salary'), reverse=True)
print_sortedobj('sort class employee by salary, reversed, using attrgetter', employees, sorted_employees)
