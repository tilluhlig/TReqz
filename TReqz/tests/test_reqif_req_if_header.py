import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifReqIfHeader(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_req_if_header()

    def test_name(self):
        self.assertEqual("REQ-IF-HEADER", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
