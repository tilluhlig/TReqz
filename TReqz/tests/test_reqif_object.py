import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifObject(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_object()

if __name__ == '__main__':
    unittest.main()
