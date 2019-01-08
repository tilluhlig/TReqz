import unittest
from libs.Requirements.TReqz.tests import utils as TE

class TestReqifDatatypeDefinition(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_datatype_definition()

    def test_decode(self):
        TE.utils.testDecodeIdentifiableAttributes(self, self.obj)

    def test_encode(self):
        TE.utils.testEncodeIdentifiableAttributes(self, self.obj)

if __name__ == '__main__':
    unittest.main()
