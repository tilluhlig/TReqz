import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifIdDict(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_id_dict()

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
