import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifSpecificationType(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_specification_type()

    def test_name(self):
        self.assertEqual("SPECIFICATION-TYPE", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
