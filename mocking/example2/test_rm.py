from mymodule import rm

import os.path
import tempfile
import unittest


class RmTestCase(unittest.TestCase):

    tmppfilepath = os.path.join(tempfile.gettempdir(), 'tmp-testfile')

    def setUp(self) -> None:
        with open(self.tmppfilepath, 'wb') as f:
            f.write(b"delete me")

    def test_rm(self):
        rm(self.tmppfilepath)
        self.assertFalse(os.path.isfile(self.tmppfilepath), 'failed to remove the file')


if __name__ == '__main__':
    unittest.main()