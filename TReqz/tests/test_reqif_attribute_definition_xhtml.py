import unittest
from . import utils as TE


class TestReqifAttributeDefinitionXhtml(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_definition_xhtml()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-DEFINITION-XHTML", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
