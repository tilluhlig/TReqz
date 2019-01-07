import unittest
import os
import shutil
import sys
from libs.Requirements import TReqz as TReqz


class TestReqif(unittest.TestCase):
    def setUp(self):
        filePath = os.path.realpath(__file__)
        self.localPath = os.path.dirname(filePath)
        self.reqif = TReqz.reqif()

    def loadExampleA(self):
        self.reqif.parseFile(self.localPath+"/../examples/exampleA/Test_000977e1.reqif")

    def test_getHeader(self):
        self.loadExampleA()
        header = self.reqif.getHeader()
        self.assertIsNotNone(header)

    def test_getReqifContainer(self):
        self.assertIsNone(self.reqif.getReqifContainer())
        self.test_parseFile()

    def test_parseFile(self):
        self.loadExampleA()
        self.assertIsNotNone(self.reqif.getReqifContainer())

    def test_dumpToFile(self):
        raise NotImplementedError

    def test_addSpecificationType(self):
        raise NotImplementedError

    def test_addDocument(self):
        raise NotImplementedError

    def test_findSpecObjectTypeIdByLongName(self):
        self.loadExampleA()
        specObjectTypeId = self.reqif.findSpecObjectTypeIdByLongName("Test_OBJECT-TYPE")
        self.assertEqual("_63d2eb9d-0ed5-42ad-af40-7564803bdf4e", specObjectTypeId)

    def test_findSpecObjectTypeByLongName(self):
        self.loadExampleA()
        specObjectType = self.reqif.findSpecObjectTypeByLongName("Test_OBJECT-TYPE")
        self.assertEqual("Test_OBJECT-TYPE", specObjectType.long_name)

    def test_findSpecObjectTypeIdByRequirementId(self):
        self.loadExampleA()
        id = self.reqif.findSpecObjectTypeIdByRequirementId("_3abe5d82-5006-4096-8dbe-874bd89225f0")
        self.assertEqual("_63d2eb9d-0ed5-42ad-af40-7564803bdf4e", id)

    def test_findSpecObjectTypeIdByAttributetTypeId(self):
        self.loadExampleA()
        id = self.reqif.findSpecObjectTypeIdByAttributetTypeId("_b74bcd4e-b697-40b6-9310-b348fdf1f02a")
        self.assertEqual("_63d2eb9d-0ed5-42ad-af40-7564803bdf4e", id)

    def test_getAllSpecObjectTypeLongNames(self):
        self.loadExampleA()
        longNames = self.reqif.getAllSpecObjectTypeLongNames()
        self.assertEqual(["Test_OBJECT-TYPE"], longNames)

    def test_getAllSpecObjectTypeIds(self):
        self.loadExampleA()
        ids = self.reqif.getAllSpecObjectTypeIds()
        self.assertEqual(["_63d2eb9d-0ed5-42ad-af40-7564803bdf4e"], ids)

    def test_findDatatypeIdByLongName(self):
        self.loadExampleA()
        id = self.reqif.findDatatypeIdByLongName("Text")
        self.assertEqual("_160c05f1-56bc-49a8-b098-a5aa79bafa8f", id)

    def test_findDatatypeByLongName(self):
        self.loadExampleA()
        dataType = self.reqif.findDatatypeByLongName("Text")
        self.assertEqual("Text", dataType.long_name)

    def test_getAllDatatypeLongNames(self):
        self.loadExampleA()
        longNames = self.reqif.getAllDatatypeLongNames()
        self.assertEqual(["Text", "REQIF_state_type", "String", "REQIF_type_type", "OEM_state_type"], longNames)

    def test_getAllDatatypeIds(self):
        self.loadExampleA()
        ids = self.reqif.getAllDatatypeIds()
        self.assertEqual(["_160c05f1-56bc-49a8-b098-a5aa79bafa8f", "_72db096a-a4bd-410a-a6d9-0f07a272f6e6", "_19962216-3130-4d5f-be28-7d50f0d381f8", "_86b444b2-75dc-4060-a25d-7f1350588f9b", "_85aa1309-3478-4fed-9b96-2f2e2ac5d417"], ids)

    def test_findAttributeTypeIdByLongName(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        attributeTypeId = self.reqif.findAttributeTypeIdByLongName(specObjectTypeIds[0], "ReqIF.Text")
        self.assertEqual("_4acbb303-ae69-44b4-b8fb-1750b1b26e8a", attributeTypeId)

    def test_findAttributeTypeByLongName(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        attributeType = self.reqif.findAttributeTypeByLongName(specObjectTypeIds[0], "ReqIF.Text")
        self.assertEqual("ReqIF.Text", attributeType.long_name)

    def test_getAllAttributeTypeLongNames(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        longNames = self.reqif.getAllAttributeTypeLongNames(specObjectTypeIds[0])
        self.assertEqual(["ReqIF.ChapterName", "ReqIF.Text", "REQIF_comment", "REQIF_state", "REQIF_object_id", "REQIF_type", "OEM_comment", "OEM_state"], longNames)

    def test_checkAttributeIsEnumeration(self):
        self.loadExampleA()
        self.assertFalse(self.reqif.checkAttributeIsEnumeration("_4acbb303-ae69-44b4-b8fb-1750b1b26e8a"))
        self.assertTrue(self.reqif.checkAttributeIsEnumeration("_80b51c6b-9152-47a2-b697-b4da03d34cd1"))

    def test_checkAttributeIsEnumerationByLongName(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        self.assertFalse(self.reqif.checkAttributeIsEnumerationByLongName(specObjectTypeIds[0], "ReqIF.Text"))
        self.assertTrue(self.reqif.checkAttributeIsEnumerationByLongName(specObjectTypeIds[0], "REQIF_type"))

    def test_convertEnumerationValues(self):
        self.loadExampleA()
        result = self.reqif.convertEnumerationValues("_80b51c6b-9152-47a2-b697-b4da03d34cd1", ["2"])
        self.assertEqual(["headline"], result)

    def test_convertEnumerationValuesByLongName(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        result = self.reqif.convertEnumerationValuesByLongName(specObjectTypeIds[0], "REQIF_type", ["2"])
        self.assertEqual(["headline"], result)

    def test_getAllAttributeTypeIds(self):
        self.loadExampleA()
        specObjectTypeIds = self.reqif.getAllSpecObjectTypeIds()
        ids = self.reqif.getAllAttributeTypeIds(specObjectTypeIds[0])
        self.assertEqual(["_b74bcd4e-b697-40b6-9310-b348fdf1f02a", "_4acbb303-ae69-44b4-b8fb-1750b1b26e8a", "_de3b5d0e-a3eb-4cde-9a77-eb1dfefc2088", "_b4132ae8-eec9-4902-83e2-3cc4bdaaa0ab", "_b5709b50-04fe-45be-9354-9246f6979a91", "_80b51c6b-9152-47a2-b697-b4da03d34cd1", "_0621d757-8f5a-49e5-991b-1b24e9620729", "_07d64d23-44f7-479f-b47f-1ea9d24e6065"], ids)

    def test_findSpecHierarchyByRequirementId(self):
        self.loadExampleA()
        ids = self.reqif.getAllDocumentIds()
        specHierarchyId = self.reqif.findSpecHierarchyByRequirementId(ids[0], "_0f807d36-241f-4079-9e8a-ae6666c35931")
        self.assertEqual("_e8f9de75-ac3b-4257-b3a8-9f9131ce0a0f", specHierarchyId)

    def test_addRequirement(self):
        raise NotImplementedError

    def test_findRequirementIdByLongName(self):
        self.loadExampleA()
        self.assertEqual("_0f807d36-241f-4079-9e8a-ae6666c35931", self.reqif.findRequirementIdByLongName("REQIF-17"))

    def test_findRequirementIdsByFieldValue(self):
        self.loadExampleA()
        res = self.reqif.findRequirementIdsByFieldValue("REQIF_object_id", "REQIF-17")
        self.assertEqual(["_0f807d36-241f-4079-9e8a-ae6666c35931"], res)

    def test_findRequirementsByFieldValue(self):
        self.loadExampleA()
        res = self.reqif.findRequirementsByFieldValue("REQIF_object_id", "REQIF-17")
        self.assertEqual(1, len(res))
        self.assertEqual("_0f807d36-241f-4079-9e8a-ae6666c35931", res[0].identifier)

    def test_getAllDocumentIds(self):
        self.loadExampleA()
        self.assertEqual(['_f230a28b-e124-4612-b2f8-3a94e0da19fb'], self.reqif.getAllDocumentIds())

    def test_getAllDocuments(self):
        self.loadExampleA()
        res = self.reqif.getAllDocuments()
        self.assertEqual("_f230a28b-e124-4612-b2f8-3a94e0da19fb", res[0].identifier)
        self.assertEqual(1, len(res))

    def test_getAllDocumentRequirementIds(self):
        self.loadExampleA()
        ids = self.reqif.getAllDocumentIds()
        res = self.reqif.getAllDocumentRequirementIds(ids[0])
        self.assertEqual(18, len(res))

    def test_getAllRequirementIds(self):
        self.loadExampleA()
        res = self.reqif.getAllRequirementIds()
        self.assertEqual(18, len(res))

    def test_getChildParentMapForDocument(self):
        raise NotImplementedError

    def test_getDocumentHierarchicalRequirementIds(self):
        self.loadExampleA()
        docIds = self.reqif.getAllDocumentIds()
        ids = self.reqif.getDocumentHierarchicalRequirementIds(docIds[0])
        self.assertEqual(["_41abd652-7ee6-4268-b711-f8619167c6b3"], list(ids.keys()))

    def test_getHierarchicalRequirementIds(self):
        self.loadExampleA()
        ids = self.reqif.getHierarchicalRequirementIds()
        self.assertEqual(["_41abd652-7ee6-4268-b711-f8619167c6b3"], list(ids.keys()))

    def test_setRequirementValues(self):
        self.loadExampleA()
        self.reqif.setRequirementValues("_0f807d36-241f-4079-9e8a-ae6666c35931", {'REQIF_object_id': "newValue"})
        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91')
        self.assertEqual("newValue", value)

    def test_setRequirementValue(self):
        self.loadExampleA()
        self.reqif.setRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91', "newValue")
        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91')
        self.assertEqual("newValue", value)

    def test_setRequirementValueByAttributeLongName(self):
        self.loadExampleA()
        self.reqif.setRequirementValueByAttributeLongName("_0f807d36-241f-4079-9e8a-ae6666c35931", "REQIF_object_id", "newValue")
        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91')
        self.assertEqual("newValue", value)

    def test_setRequirementValueByLongNames(self):
        self.loadExampleA()
        self.reqif.setRequirementValueByLongNames("REQIF-17", "REQIF_object_id", "newValue")
        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91')
        self.assertEqual("newValue", value)

    def test_getRequirementValue(self):
        self.loadExampleA()
        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", '_b5709b50-04fe-45be-9354-9246f6979a91')
        self.assertEqual("REQIF-17", value)

        value = self.reqif.getRequirementValue("_0f807d36-241f-4079-9e8a-ae6666c35931", 'no_attribute_identifier', "test_value")
        self.assertEqual("test_value", value)

    def test_getRequirementValueByAttributeLongName(self):
        self.loadExampleA()
        value = self.reqif.getRequirementValueByAttributeLongName("_0f807d36-241f-4079-9e8a-ae6666c35931", 'REQIF_object_id')
        self.assertEqual("REQIF-17", value)

        value = self.reqif.getRequirementValueByAttributeLongName("_0f807d36-241f-4079-9e8a-ae6666c35931", 'no_attribute_identifier', "test_value")
        self.assertEqual("test_value", value)

    def test_getRequirementValueByLongNames(self):
        self.loadExampleA()
        value = self.reqif.getRequirementValueByLongNames("REQIF-17", 'REQIF_object_id')
        self.assertEqual("REQIF-17", value)

        value = self.reqif.getRequirementValueByLongNames("REQIF-17", 'no_attribute', "test_value")
        self.assertEqual("test_value", value)

    def test_getRequirementValues(self):
        self.loadExampleA()
        values = self.reqif.getRequirementValues("_0f807d36-241f-4079-9e8a-ae6666c35931")
        self.assertEqual("REQIF-17", values['REQIF_object_id'])

    def test_getRequirementValuesByLongName(self):
        self.loadExampleA()
        values = self.reqif.getRequirementValuesByLongName("REQIF-17")
        self.assertEqual("REQIF-17", values['REQIF_object_id'])

    def test_getObject(self):
        self.loadExampleA()
        obj = self.reqif.getObject("_0f807d36-241f-4079-9e8a-ae6666c35931")
        self.assertEqual("_0f807d36-241f-4079-9e8a-ae6666c35931", obj.identifier)


if __name__ == '__main__':
    unittest.main()
