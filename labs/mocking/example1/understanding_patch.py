from unittest.mock import patch
from modules.employee_test import Employee

e = Employee('first', 'last', 10)
print(f'e.email = {e.email}\n')
print('---------------------------------------------------------------------------------------------------------')
# with patch('modules.employee.Employee.email') as me:
#     me.return_value = "ciao"
#     print(f'e.email = {e.email}\n')

print(f'unmocked e.getsomestring(): {e.getsomestring()}')


class Test():
    def patchmodule(self):
        with patch('modules.employee_test.Employee.getsomestring') as me:
            me.return_value = "ciao"
            mgss = e.getsomestring()
            print('\tfrom patch: modules.employee_test.Employee.getsomestring')
            print(f'\tmocked e.getsomestring(): {mgss}')
            print()

            print(f'unmocked e.getsomestring(): {e.getsomestring()}')

    def patchscript(self):
        with patch('understanding_patch.Employee.getsomestring') as me:
            me.return_value = "ciao"
            mgss = e.getsomestring()
            print('\tfrom patch: understanding_patch.Employee.getsomestring')
            print(f'\tmocked e.getsomestring(): {mgss}')
            print()

            print(f'unmocked e.getsomestring(): {e.getsomestring()}')

    # def patchclass(self):
    #     with patch('Employee.getsomestring') as me:
    #         me.return_value = "ciao"
    #         mgss = e.getsomestring()
    #         print('\tfrom patch: understanding_patch.Employee.getsomestring')
    #         print(f'\tmocked e.getsomestring(): {mgss}')
    #         print()
    #
    #         print(f'unmocked e.getsomestring(): {e.getsomestring()}')


t = Test()

# t.patchmodule()
# t.patchscript()
t.patchclass()

