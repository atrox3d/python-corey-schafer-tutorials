from modules import utils


class Employee:
    raise_amount = 1.04
    count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@company.com'

        Employee.count += 1

    def fullname(self):
        return f'{self.first}, {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def print_salary(self):
        print(
            f'{self.__class__.__name__:<10} | '
            f'{self.fullname():<10}: pay={self.pay}, raise amount={self.raise_amount!s:>4} | '
            f'dict= {self.__dict__}'
        )

    @classmethod
    def from_string(cls, emp_str, sep=';'):
        first, last, pay = emp_str.split(sep)
        emp = cls(first, last, pay)
        return emp


class Developer(Employee):
    #
    #   overrides Employee.raise_amount
    #
    raise_amount = 1.10

    def __init__(self, first, last, pay, language):
        # initializes underlying Employee instance
        super().__init__(first, last, pay)  # same as Employee.__init__(first, last, pay)
        self.language = language


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        # initializes underlying Employee instance
        super().__init__(first, last, pay)  # same as Employee.__init__(first, last, pay)
        self.employees = [] if employees is None else employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
            print(f'-->{employee.fullname()}')


emp1 = Employee('bob', 'red', 5000)
dev1 = Developer('kate', 'blue', 5500, 'python')
mgr1 = Manager('sue', 'smith', 90000, [dev1])

utils.banner('print salaries')
emp1.print_salary()
dev1.print_salary()
mgr1.print_salary()

utils.banner('print manager\'s employees')
mgr1.add_employee(emp1)
mgr1.print_employees()

utils.banner('print manager\'s employees')
mgr1.remove_employee(dev1)
mgr1.print_employees()

utils.banner('isinstance()')
print(f'                          {"Employee":<20}{"Developer":<20}{"Manager":<20}')
obj = emp1
cls = Employee
print(f'employee |isinsstance     {isinstance(obj, Employee)!s:<20}{isinstance(obj, Developer)!s:<20}{isinstance(obj, Manager)!s:<20}')
print(f'Employee |issubclass      {issubclass(cls, Employee)!s:<20}{issubclass(cls, Developer)!s:<20}{issubclass(cls, Manager)!s:<20}')
obj = dev1
cls = Developer
print(f'developer|isinsstance     {isinstance(obj, Employee)!s:<20}{isinstance(obj, Developer)!s:<20}{isinstance(obj, Manager)!s:<20}')
print(f'developer|issubclass      {issubclass(cls, Employee)!s:<20}{issubclass(cls, Developer)!s:<20}{issubclass(cls, Manager)!s:<20}')
obj = mgr1
cls = Manager
print(f'manager  |isinsstance     {isinstance(obj, Employee)!s:<20}{isinstance(obj, Developer)!s:<20}{isinstance(obj, Manager)!s:<20}')
print(f'manager  |issubclass      {issubclass(cls, Employee)!s:<20}{issubclass(cls, Developer)!s:<20}{issubclass(cls, Manager)!s:<20}')
