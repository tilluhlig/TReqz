import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifDatatypeDefinitionXhtml(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_datatype_definition_xhtml()

    def test_name(self):
        self.assertEqual("DATATYPE-DEFINITION-XHTML", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
