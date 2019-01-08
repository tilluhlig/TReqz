import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifIdentifiable(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_identifiable()

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
