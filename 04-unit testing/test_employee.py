import unittest
from unittest.mock import patch
# from employee_test import Employee
from modules import employee_test
import employee
import logging


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.log.info('setUp')
        # print('setUp')

        # self.emp_1 = employee_test.Employee('Corey', 'Schafer', 50000)
        # self.emp_2 = employee_test.Employee('Sue', 'Smith', 60000)

        self.emp_1 = employee.Employee('Corey', 'Schafer', 50000)
        self.emp_2 = employee.Employee('Sue', 'Smith', 60000)

    def tearDown(self):
        self.log.info('tearDown\n')

    @classmethod
    def setUpClass(cls):
        formatstring = '%(asctime)s | %(levelname)-10s | %(name)s | %(funcName)s | %(message)s'
        formatter = logging.Formatter(formatstring)  # get formatter
        cli_handler = logging.StreamHandler()  # get CLI handler (default=stderr)
        cli_handler.setFormatter(formatter)  # set formatter for CLI handler

        cls.log = logging.getLogger(cls.__name__)
        cls.log.setLevel(logging.DEBUG)
        cls.log.addHandler(cli_handler)  # add CLI handler to logger
        cls.log.info('setupClass')

    @classmethod
    def tearDownClass(cls):
        cls.log.info('tearDownClass')

    def test_email(self):
        self.log.info('test_email')

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.log.info('test_fullname')

        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.log.info('test_apply_raises')

        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        #
        #   create context manager inside employee class
        #
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')

    def test_wtf(self):
        import os

        with patch('os.getcwd') as mocked_getcwd:
            mocked_getcwd.return_value = "ciao"
            self.log.info(os.getcwd())


if __name__ == '__main__':
    import os

    _getcwd = os.getcwd
    print(_getcwd())


    def cwd():
        return "ciaone"


    os.getcwd = cwd

    print(os.getcwd())

    unittest.main()
