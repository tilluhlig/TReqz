import unittest
from . import utils as TE


class TestReqifDatatypeDefinitionXhtml(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_datatype_definition_xhtml()

    def test_name(self):
        self.assertEqual("DATATYPE-DEFINITION-XHTML", self.obj.name)

    def test_decode(self):
        TE.utils.testDecodeIdentifiableAttributes(self, self.obj)

    def test_encode(self):
        TE.utils.testEncodeIdentifiableAttributes(self, self.obj)

if __name__ == '__main__':
    unittest.main()
