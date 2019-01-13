import unittest
from . import utils as TE


class TestReqifAttributeValueXhtml(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_value_xhtml()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-VALUE-XHTML", self.obj.name)

    def test_decode(self):
        TE.utils.testDecodeLocalRefFromElementText(self, self.obj, "<DEFINITION><ATTRIBUTE-DEFINITION-XHTML-REF>1</ATTRIBUTE-DEFINITION-XHTML-REF></DEFINITION>", "definition", "1")
        TE.utils.testDecodeAttribute(self, self.obj, 'the_value', 'THE-VALUE')
        TE.utils.testDecodeAttribute(self, self.obj, 'the_original_value', 'THE-ORIGINAL-VALUe')
        TE.utils.testDecodeAttribute(self, self.obj, 'is_simplified', 'IS-SIMPLIFIED')

    def test_encode(self):
        TE.utils.testEncodeLocalRefFromElementText(self, self.obj, "<DEFINITION><ATTRIBUTE-DEFINITION-XHTML-REF>1</ATTRIBUTE-DEFINITION-XHTML-REF></DEFINITION>", "definition", "1")
        TE.utils.testEncodeAttribute(self, self.obj, 'the_value', 'THE-VALUE')
        TE.utils.testEncodeAttribute(self, self.obj, 'the_original_value', 'THE-ORIGINAL-VALUe')
        TE.utils.testEncodeAttribute(self, self.obj, 'is_simplified', 'IS-SIMPLIFIED')

if __name__ == '__main__':
    unittest.main()
