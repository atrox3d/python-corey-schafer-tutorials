"""
https://www.toptal.com/python/an-introduction-to-mocking-in-python
"""
from mymodule import RemovalService, UploadService

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

    @mock.patch('mymodule.os.path')  # second decorator
    @mock.patch('mymodule.os')  # first decorator
    def test_rm_decorator(self, mock_os, mock_path):
        reference = RemovalService()  # instantiate RemovalService

        mock_path.isfile.return_value = False  # setup the mock: file does not exist

        reference.rm("any path")  # test object not to delete

        self.assertFalse(  # test that the remove call was NOT called
            mock_os.remove.called,
            "failed to not remove the file if not present"
        )

        mock_path.isfile.return_value = True  # make the file exist

        reference.rm("any path")  # test again: fake delete

        mock_os.remove.assert_called_with("any path")  # check argument

    def test_rm_context(self):
        with mock.patch('mymodule.os') as mock_os:
            with mock.patch('mymodule.os.path') as mock_path:
                reference = RemovalService()  # instantiate RemovalService

                mock_path.isfile.return_value = False  # setup the mock: file does not exist

                reference.rm("any path")  # test object not to delete

                self.assertFalse(  # test that the remove call was NOT called
                    mock_os.remove.called,
                    "failed to not remove the file if not present"
                )

                mock_path.isfile.return_value = True  # make the file exist

                reference.rm("any path")  # test again: fake delete

                mock_os.remove.assert_called_with("any path")  # check argument


class UploadServiceTestCase(unittest.TestCase):

    """
    OPTION 1: MOCKING INSTANCE METHODS
    """
    @mock.patch.object(RemovalService, 'rm')
    def test_upload_complete(self, mock_rm):
        # build our dependencies
        removal_service = RemovalService()
        reference = UploadService(removal_service)

        # call upload_complete, which shoul, in turn, 'rm'
        reference.upload_complete("my uploaded file")

        # check that it called the rm method of any RemovalService
        mock_rm.assert_called_with("my uploaded file")

        # check that it called the rm of _our_ removal_service
        removal_service.rm.assert_called_with("my uploaded file")

        # my check: is mock_rm the same as removal_service.rm?
        print(mock_rm is removal_service.rm)


if __name__ == '__main__':
    unittest.main()
