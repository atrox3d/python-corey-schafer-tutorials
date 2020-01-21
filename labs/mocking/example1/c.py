# import mocking.a
from labs.mocking.example1 import a
from unittest.mock import patch

sc = a.SomeClass()
print(f'MAIN: {sc.getvalue()}')

with patch('a.SomeClass.getvalue') as getvalue:
    getvalue.return_value = 'mockedvalue'
    # sc.printvalue()
    print(f'\nPATCH:a.SomeClass.getvalue: {sc.getvalue()}')

with patch('a.SomeClass') as psc:
    psc.value = 'mockedvalue'
    print(f'\nPATCH:a.SomeClass: {sc.getvalue()}')

with patch('__main__.a.SomeClass.getvalue') as getvalue:
    getvalue.return_value = 'mockedvalue'
    print(f'\nPATCH:__main__.a.SomeClass.getvalue: {sc.getvalue()}')

with patch('mocking.example1.a.SomeClass.getvalue') as getvalue:
    getvalue.return_value = 'mockedvalue'
    print(f'\nPATCH:mocking.a.SomeClass.getvalue: {sc.getvalue()}')

# with patch('SomeClass.getvalue') as getvalue:
#     getvalue.return_value = 'mockedvalue'
#     print(f'\nSomeClass.getvalue: {sc.getvalue()}')

print(f'\nMAIN: {sc.getvalue()}')
