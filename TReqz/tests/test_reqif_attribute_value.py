import unittest
from libs.Requirements.TReqz.tests import utils as TE


class TestReqifAttributeValue(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_attribute_value()

    def test_name(self):
        self.assertEqual("ATTRIBUTE-VALUE", self.obj.name)

    def test_decode(self):
        raise NotImplementedError

    def test_encode(self):
        raise NotImplementedError

    def test_getValue(self):
        raise NotImplementedError

    def test_setValue(self):
        raise NotImplementedError

    def test_isEmpty(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
