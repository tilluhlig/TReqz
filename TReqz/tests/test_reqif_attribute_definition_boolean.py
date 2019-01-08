import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifAttributeDefinitionBoolean(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_definition_boolean()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-DEFINITION-BOOLEAN", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
