import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifReqIf(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_req_if()

    def test_name(self):
        self.assertEqual("REQ-IF", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
