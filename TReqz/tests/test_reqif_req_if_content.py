import unittest
from . import utils as TE


class TestReqifReqIfContent(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_req_if_content()

    def test_name(self):
        self.assertEqual("REQ-IF-CONTENT", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
