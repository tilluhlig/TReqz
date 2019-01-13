import unittest
from . import utils as TE


class TestReqifAttributeDefinitionEnumeration(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_definition_enumeration()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-DEFINITION-ENUMERATION", self.obj.name)

    def test_decode(self):
        TE.utils.testDecodeLocalRefFromElementText(self, self.obj, "<TYPE><DATATYPE-DEFINITION-ENUMERATION-REF>1</DATATYPE-DEFINITION-ENUMERATION-REF></TYPE>", "type", "1")
        TE.utils.testDecodeObjectByElementClass(self, self.obj, "<DEFAULT-VALUE><ATTRIBUTE-VALUE-ENUMERATION /></DEFAULT-VALUE>", "default_value", "ATTRIBUTE-VALUE-ENUMERATION")
        TE.utils.testDecodeAttribute(self, self.obj, 'is_editable', 'IS-EDITABLE')

    def test_encode(self):
        TE.utils.testEncodeLocalRefFromElementText(self, self.obj, "<TYPE><DATATYPE-DEFINITION-ENUMERATION-REF>1</DATATYPE-DEFINITION-ENUMERATION-REF></TYPE>", "type", "1")
        TE.utils.testEncodeObjectByElementClass(self, self.obj, "<DEFAULT-VALUE><ATTRIBUTE-VALUE-ENUMERATION /></DEFAULT-VALUE>", "default_value", TE.TReqz.reqif_attribute_value_enumeration())
        TE.utils.testEncodeAttribute(self, self.obj, 'is_editable', 'IS-EDITABLE')

    def test_getValueMap(self):
        raise NotImplementedError

    def test_getReversedValueMap(self):
        raise NotImplementedError

    def test_getValueMapWithEnumObjects(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
