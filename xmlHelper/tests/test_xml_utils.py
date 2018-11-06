import unittest
from xmlHelper import xml_utils as xml_utils
import re


class TestXmlUtils(unittest.TestCase):

    def test_get_tag_name(self):
        values = [["A", "A"],
                  ["A", "{}A"],
                  ["A", "{A}A"],
                  ["A", "{html:aa}A"],
                  ["", "{}"],
                  ["", None]]
        for value in values:
            self.assertEqual(xml_utils.get_tag_name(value[1]), value[0])

    def test_check_tag_name(self):
        values = [[True, "A", "A"],
                  [True, "{}A", "A"],
                  [True, "{A}A", "A"],
                  [True, "{html:aa}A", "A"],
                  [False, "{}", "A"],
                  [False, None, "A"],
                  [False, "{}A", "B"],
                  [False, "A", "B"],
                  [False, "{html:aa}A", "B"],
                  [False, "{}A", None],
                  [False, None, "A"],
                  [True, None, ""]]
        for value in values:
            self.assertEqual(xml_utils.check_tag_name(
                value[1], value[2]), value[0])

    def test_get_tag_namespace(self):
        values = [["", "A"],
                  ["{}", "{}A"],
                  ["{A}", "{A}A"],
                  ["{html:aa}", "{html:aa}A"],
                  ["{}", "{}"],
                  ["", None]]
        for value in values:
            self.assertEqual(xml_utils.get_tag_namespace(value[1]), value[0])

    def test_get_text_from_element(self):
        raise NotImplementedError

    def test_get_element(self):
        raise NotImplementedError

    def test_current_timestamp(self):
        raise NotImplementedError

    def test_merge_elements(self):
        raise NotImplementedError

    def test_setElementAttribute(self):
        raise NotImplementedError

    def test_createSubElement(self):
        raise NotImplementedError

    def test_addRequiredSubElement(self):
        raise NotImplementedError

    def test_addEncodedSubElement(self):
        raise NotImplementedError

    def test_generateMd5(self):
        res = xml_utils.generateMd5('A')
        res2 = xml_utils.generateMd5('A')
        self.assertEqual(res, res2)
        res3 = xml_utils.generateMd5('BB')
        self.assertNotEqual(res, res3)
        self.assertTrue(re.match("^[a-f0-9]{32}$", res))

    def test_validateXmlFile(self):
        raise NotImplementedError

    def test_decodeXhtml(self):
        raise NotImplementedError

    def test_encodeXhtml(self):
        raise NotImplementedError

    def test_stringIsWellFormedXml(self):
        self.assertFalse(xml_utils.stringIsWellFormedXml(""))
        self.assertFalse(xml_utils.stringIsWellFormedXml(None))
        self.assertTrue(xml_utils.stringIsWellFormedXml("<a></a>"))
        self.assertFalse(xml_utils.stringIsWellFormedXml("<a>"))
        self.assertFalse(xml_utils.stringIsWellFormedXml("<a></a>abc"))

    def test_normalizeXhtml(self):
        values = [["", ""],
                  [None, None],
                  ["<html:div>AA</html:div>", "AA"],
                  ["<img src=\"abc/asas.png\">AA</img>", "AA"],
                  ["A\nA", "AA"],
                  ["<a><b><c>AA</a>", "AA"],
                  ["AA A", "AA A"]]
        for value in values:
            self.assertEqual(xml_utils.normalizeXhtml(value[0]), value[1])


if __name__ == '__main__':
    unittest.main()
