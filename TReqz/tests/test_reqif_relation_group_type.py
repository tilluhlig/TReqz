import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifRelationGroupType(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_relation_group_type()

    def test_name(self):
        self.assertEqual("RELATION-GROUP-TYPE", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
