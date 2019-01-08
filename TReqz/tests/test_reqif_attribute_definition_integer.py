import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifAttributeDefinitionInteger(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_definition_integer()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-DEFINITION-INTEGER", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
