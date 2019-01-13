import unittest
from . import utils as TE


class TestReqifSpecRelation(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_spec_relation()

    def test_name(self):
        self.assertEqual("SPEC-RELATION", self.obj.name)

    def test_decode(self):
        TE.utils.testDecodeIdentifiableAttributes(self, self.obj)
        TE.utils.testDecodeLocalRefFromElementText(self, self.obj, "<SOURCE><SPEC-OBJECT-REF>1</SPEC-OBJECT-REF></SOURCE>", "source", "1")
        TE.utils.testDecodeLocalRefFromElementText(self, self.obj, "<TARGET><SPEC-OBJECT-REF>1</SPEC-OBJECT-REF></TARGET>", "target", "1")
        TE.utils.testDecodeLocalRefFromElementText(self, self.obj, "<TYPE><SPEC-RELATION-TYPE-REF>1</SPEC-RELATION-TYPE-REF></TYPE>", "type", "1")

        for TAG, CLASS in TE.TReqz.reqif_config.ATTRIBUTE_VALUE_TAG_TO_CLASS.items():
            TE.utils.testDecodeObjectListByElementClass(self, self.obj, "<VALUES><"+TAG+" /></VALUES>", "values", [TAG])
            TE.utils.testDecodeObjectListByElementClass(self, self.obj, "<VALUES><"+TAG+" /><"+TAG+" /></VALUES>", "values", [TAG, TAG])
            TE.utils.testDecodeObjectListByElementClass(self, self.obj, "<VALUES></VALUES>", "values", [])

    def test_encode(self):
        TE.utils.testEncodeIdentifiableAttributes(self, self.obj)
        TE.utils.testEncodeLocalRefFromElementText(self, self.obj, "<SOURCE><SPEC-OBJECT-REF>1</SPEC-OBJECT-REF></SOURCE>", "source", "1")
        TE.utils.testEncodeLocalRefFromElementText(self, self.obj, "<TARGET><SPEC-OBJECT-REF>1</SPEC-OBJECT-REF></TARGET>", "target", "1")
        TE.utils.testEncodeLocalRefFromElementText(self, self.obj, "<TYPE><SPEC-RELATION-TYPE-REF>1</SPEC-RELATION-TYPE-REF></TYPE>", "type", "1")

        for TAG, CLASS in TE.TReqz.reqif_config.ATTRIBUTE_VALUE_TAG_TO_CLASS.items():
            TE.utils.testEncodeObjectListByElementClass(self, self.obj, "<VALUES><"+TAG+" /></VALUES>", "values", [CLASS])
            TE.utils.testEncodeObjectListByElementClass(self, self.obj, "<VALUES><"+TAG+" /><"+TAG+" /></VALUES>", "values", [CLASS, CLASS])
            TE.utils.testEncodeObjectListByElementClass(self, self.obj, "", "values", [])

if __name__ == '__main__':
    unittest.main()
