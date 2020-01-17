"""
https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""
from mymodule import rm

import os.path
import tempfile
import unittest
from unittest import mock


class RmTestCase(unittest.TestCase):
    tmppfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self) -> None:
        with open(self.tmppfilepath, 'wb') as f:
            f.write(b"delete me")

    @mock.patch('mymodule.os')
    def test_rm_decorator(self, mock_os):
        rm("any path")
        # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
        mock_os.remove.assert_called_with("any path")

    def test_rm_context(self):
        with mock.patch('mymodule.os') as mock_os:
            rm("any path")
            # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
            mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
