from modules import utils


class Employee:
    pass


emp1 = Employee()
emp2 = Employee()

utils.printfvar(emp1, 'emp1')
utils.printfvar(emp2, 'emp2')

emp1.name = 'bob'
print(emp1.name)
