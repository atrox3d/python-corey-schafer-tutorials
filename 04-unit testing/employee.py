import requests
from modules import logger


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        self.log = logger.getCLIlogger(self.__class__.__name__)
        self.log.info(f'{first}, {last}, {pay}')

    @property
    def email(self):
        email = '{}.{}@email.com'.format(self.first, self.last)
        self.log.info(email)
        return email

    @property
    def fullname(self):
        fullname = '{} {}'.format(self.first, self.last)
        self.log.info(fullname)
        return fullname

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get(f'http://company.com/{self.last}/{month}')
        self.log.info(f'response = {response}')
        self.log.info(f'response.ok = {response.ok}')
        self.log.info(f'response.text = {response.text}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


if __name__ == '__main__':
    e = Employee('first', 'last', 1000)
