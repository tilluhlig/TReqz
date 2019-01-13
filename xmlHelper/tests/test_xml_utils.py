import unittest
from .. import xml_utils as xml_utils
import xml.etree.ElementTree as ET
import re
import time


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
        res = xml_utils.get_text_from_element(ET.fromstring("<a><b>text</b>abc</a>"), "./b")
        self.assertEqual("text", res)

        res = xml_utils.get_text_from_element(ET.fromstring("<a><b>text</b></a>"), ".")
        self.assertEqual(None, res)

        res = xml_utils.get_text_from_element(ET.fromstring("<a>abc<b>text</b></a>"), ".")
        self.assertEqual("abc", res)

    def test_get_element(self):
        res = xml_utils.get_element(ET.fromstring("<a><b>text</b>abc</a>"), "./b")
        self.assertEqual("b", res.tag)

        res = xml_utils.get_element(ET.fromstring("<a><b>text</b></a>"), ".")
        self.assertEqual("a", res.tag)

        res = xml_utils.get_element(ET.fromstring("<a>abc<b>text</b></a>"), "./b/c")
        self.assertEqual(None, res)

    def test_current_timestamp(self):
        firstTimestamp = xml_utils.current_timestamp()
        time.sleep(1)
        secondTimestamp = xml_utils.current_timestamp()
        self.assertNotEqual(firstTimestamp, secondTimestamp)

    def test_merge_elements(self):
        raise NotImplementedError

    def test_setElementAttribute(self):
        elem = xml_utils.createSubElement("element")
        xml_utils.setElementAttribute(elem, "attrib", "value")
        self.assertEqual("value", elem.get("attrib"))
        xml_utils.setElementAttribute(elem, "attrib", "value2")
        self.assertEqual("value2", elem.get("attrib"))
        xml_utils.setElementAttribute(elem, "attrib", None)
        self.assertEqual("value2", elem.get("attrib"))

    def test_createSubElement(self):
        elem = xml_utils.createSubElement("element")
        self.assertEqual("element", elem.tag)
        self.assertEqual(None, elem.text)

        elem2 = xml_utils.createSubElement("element", "content")
        self.assertEqual("element", elem2.tag)
        self.assertEqual("content", elem2.text)

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
