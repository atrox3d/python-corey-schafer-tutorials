###################################################################################################
#   https://youtu.be/6tNS--WetLI
###################################################################################################
"""
this is the test unit for module calc.py
it is conventionally named test_*

HOW TO RUN:
    1)  without the "if __name__ == '__main__" test:
            python -m unittest test_calc.py

    2) adding the __main__ section just run
            python test_calc.py

    3) PyCharm: ALT+SHIFT+F10: select unittests in test_calc.py
"""
import unittest  # std library
import calc  # in pycharm: right click on folder/mark as/Sources Root

"""
https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug
----------------------------+--------------------------------------------
Method					    |	Checks that
----------------------------+--------------------------------------------
assertEqual(a, b)		    |	a == b
assertNotEqual(a, b)	    |	a != b
assertTrue(x)			    |	bool(x) is True
assertFalse(x)			    |	bool(x) is False
assertIs(a, b)			    |	a is b
assertIsNot(a, b)		    |	a is not b
assertIsNone(x)			    |	x is None
assertIsNotNone(x)		    |	x is not None
assertIn(a, b)			    |	a in b
assertNotIn(a, b)		    |	a not in b
assertIsInstance(a, b)	    |	isinstance(a, b)
assertNotIsInstance(a, b)   |	not isinstance(a, b)
----------------------------+--------------------------------------------
"""


class TestCalc(unittest.TestCase):
    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15)


if __name__ == '__main__':
    unittest.main()
