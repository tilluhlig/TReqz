import unittest
from libs.Requirements.TReqz.tests import utils as TE
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element as Element


class TestReqifDatatypeDefinitionString(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_datatype_definition_string()

    def test_name(self):
        self.assertEqual("DATATYPE-DEFINITION-STRING", self.obj.name)

    def test_decode(self):
        TE.utils.testIdentifiableDecodeAttributes(self, self.obj)
        TE.utils.testDecodeAttribute(self, self.obj, 'max_length', 'MAX-LENGTH')

    def test_encode(self):
        TE.utils.testIdentifiableEncodeAttributes(self, self.obj)
        TE.utils.testEncodeAttribute(self, self.obj, 'max_length', 'MAX-LENGTH')

if __name__ == '__main__':
    unittest.main()
