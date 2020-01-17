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

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm_decorator(self, mock_os, mock_path):
        # print(mock_os, mock_path)

        # setup the mock
        mock_path.isfile.return_value = False

        rm("any path")

        # test that the remove call was NOT called
        self.assertFalse(
            mock_os.remove.called,
            "failed to not remove the file if not present"
        )

        # make the file exist
        mock_path.isfile.return_value = True

        rm("any path")

        # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
        mock_os.remove.assert_called_with("any path")

    def test_rm_context(self):
        with mock.patch('mymodule.os') as mock_os:
            with mock.patch('mymodule.os.path') as mock_path:
                # print(mock_os, mock_path)

                # setup the mock
                mock_path.isfile.return_value = False

                rm("any path")

                # test that the remove call was NOT called
                self.assertFalse(
                    mock_os.remove.called,
                    "failed to not remove the file if not present"
                )

                # make the file exist
                mock_path.isfile.return_value = True

                rm("any path")

                # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
                mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
