"""
https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""
from mymodule import RemovalService

import os.path
import tempfile
import unittest
from unittest import mock


class RemovalServiceTestCase(unittest.TestCase):
    tmppfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self) -> None:
        with open(self.tmppfilepath, 'wb') as f:
            f.write(b"delete me")

    """
    MOCK PATCH PITFALL: DECORATOR ORDER
    When using multiple decorators on your test methods, order is important, and it’s kind of confusing. 
    Basically, when mapping decorators to method parameters, work backwards. Consider this example:
    
        @mock.patch('mymodule.sys')
        @mock.patch('mymodule.os')
        @mock.patch('mymodule.os.path')
        def test_something(self, mock_os_path, mock_os, mock_sys):
            pass
    Notice how our parameters are matched to the reverse order of the decorators? 
    That’s partly because of the way that Python works. With multiple method decorators, 
    here’s the order of execution in pseudocode:
    
    patch_sys(patch_os(patch_os_path(test_something)))
    Since the patch to sys is the outermost patch, it will be executed last, 
    making it the last parameter in the actual test method arguments. 
    Take note of this well and use a debugger when running your tests to make sure that the right parameters are being 
    injected in the right order.    
    """

    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm_decorator(self, mock_os, mock_path):
        reference = RemovalService()
        # setup the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was NOT called
        self.assertFalse(
            mock_os.remove.called,
            "failed to not remove the file if not present"
        )

        # make the file exist
        mock_path.isfile.return_value = True

        reference.rm("any path")

        # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
        mock_os.remove.assert_called_with("any path")

    def test_rm_context(self):
        with mock.patch('mymodule.os') as mock_os:
            with mock.patch('mymodule.os.path') as mock_path:
                # print(mock_os, mock_path)
                reference = RemovalService()

                reference.rm("any path")

                # test that the remove call was NOT called
                self.assertFalse(
                    mock_os.remove.called,
                    "failed to not remove the file if not present"
                )

                # make the file exist
                mock_path.isfile.return_value = True

                reference.rm("any path")

                # self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')
                mock_os.remove.assert_called_with("any path")


if __name__ == '__main__':
    unittest.main()
