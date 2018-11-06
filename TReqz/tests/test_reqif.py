import unittest
import TReqz


class TestReqif(unittest.TestCase):
    def setUp(self):
        self.reqif = TReqz.reqif()

    def test_getHeader(self):
        raise NotImplementedError

    def test_parseFile(self):
        raise NotImplementedError

    def test_dumpToFile(self):
        raise NotImplementedError

    def test_addSpecificationType(self):
        raise NotImplementedError

    def test_addDocument(self):
        raise NotImplementedError

    def test_findSpecObjectTypeIdByLongName(self):
        raise NotImplementedError

    def test_findSpecObjectTypeByLongName(self):
        raise NotImplementedError

    def test_findSpecObjectTypeIdByRequirementId(self):
        raise NotImplementedError

    def test_findSpecObjectTypeIdByAttributetTypeId(self):
        raise NotImplementedError

    def test_getAllSpecObjectTypeLongNames(self):
        raise NotImplementedError

    def test_getAllSpecObjectTypeIds(self):
        raise NotImplementedError

    def test_findDatatypeIdByLongName(self):
        raise NotImplementedError

    def test_findDatatypeByLongName(self):
        raise NotImplementedError

    def test_getAllDatatypeLongNames(self):
        raise NotImplementedError

    def test_getAllDatatypeIds(self):
        raise NotImplementedError

    def test_findAttributeTypeIdByLongName(self):
        raise NotImplementedError

    def test_findAttributeTypeByLongName(self):
        raise NotImplementedError

    def test_getAllAttributeTypeLongNames(self):
        raise NotImplementedError

    def test_checkAttributeIsEnumeration(self):
        raise NotImplementedError

    def test_checkAttributeIsEnumerationByLongName(self):
        raise NotImplementedError

    def test_convertEnumerationValues(self):
        raise NotImplementedError

    def test_convertEnumerationValuesByLongName(self):
        raise NotImplementedError

    def test_getAllAttributeTypeIds(self):
        raise NotImplementedError

    def test_findSpecHierarchyByRequirementId(self):
        raise NotImplementedError

    def test_addRequirement(self):
        raise NotImplementedError

    def test_findRequirementIdByLongName(self):
        raise NotImplementedError

    def test_findRequirementIdsByFieldValue(self):
        raise NotImplementedError

    def test_findRequirementsByFieldValue(self):
        raise NotImplementedError

    def test_getAllDocumentIds(self):
        raise NotImplementedError

    def test_getAllDocuments(self):
        raise NotImplementedError

    def test_getAllDocumentRequirementIds(self):
        raise NotImplementedError

    def test_getAllRequirementIds(self):
        raise NotImplementedError

    def test_getChildParentMapForDocument(self):
        raise NotImplementedError

    def test_getDocumentHierarchicalRequirementIds(self):
        raise NotImplementedError

    def test_getHierarchicalRequirementIds(self):
        raise NotImplementedError

    def test_setRequirementValues(self):
        raise NotImplementedError

    def test_setRequirementValue(self):
        raise NotImplementedError

    def test_setRequirementValueByAttributeLongName(self):
        raise NotImplementedError

    def test_setRequirementValueByLongNames(self):
        raise NotImplementedError

    def test_getRequirementValue(self):
        raise NotImplementedError

    def test_getRequirementValueByAttributeLongName(self):
        raise NotImplementedError

    def test_getRequirementValueByLongNames(self):
        raise NotImplementedError

    def test_getRequirementValues(self):
        raise NotImplementedError

    def test_getRequirementValuesByLongName(self):
        raise NotImplementedError

    def test_getObject(self):
        raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
