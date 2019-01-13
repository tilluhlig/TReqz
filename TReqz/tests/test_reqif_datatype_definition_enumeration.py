import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifDatatypeDefinitionEnumeration(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_datatype_definition_enumeration()

    def test_name(self):
        self.assertEqual("DATATYPE-DEFINITION-ENUMERATION", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
