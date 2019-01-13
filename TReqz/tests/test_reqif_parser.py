import unittest
from . import utils as TE


class TestReqifParser(unittest.TestCase):
    def setUp(self):
        pass

    def test_parseFile(self):
        raise NotImplementedError

    def test_parse(self):
        parser = TE.TReqz.reqif_parser()
        elem = parser.parse("<REQ-IF></REQ-IF>")
        self.assertIsInstance(elem,TE.TReqz.reqif_req_if)

    def test_dump(self):
        parser = TE.TReqz.reqif_parser()
        with self.assertRaises(RuntimeError):
            xmlContent = parser.dump(None)

        elem = parser.parse("<REQ-IF></REQ-IF>")
        xmlContent = parser.dump(elem)
        self.assertNotEqual("", xmlContent)
        self.assertNotEqual(None, xmlContent)

    def test_dumpToFile(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
