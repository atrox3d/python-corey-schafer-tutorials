###################################################################################################
#   https://youtu.be/6tNS--WetLI
###################################################################################################
"""
this is the test unit for module calc.py
it is conventionally named test_*
"""
import unittest     # std library
import calc         # in pycharm: right click on folder/mark as/Sources Root


class TestCalc(unittest.TestCase):
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
    def test_add(self):
        pass
