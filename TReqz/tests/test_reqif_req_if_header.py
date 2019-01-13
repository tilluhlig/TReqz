import unittest
from . import utils as TE


class TestReqifReqIfHeader(unittest.TestCase):
    def setUp(self):
        self.obj = TE.TReqz.reqif_req_if_header()

    def test_name(self):
        self.assertEqual("REQ-IF-HEADER", self.obj.name)

    def test_decode(self):
        TE.utils.testDecodeAttribute(self, self.obj, 'identifier', 'IDENTIFIER')
        TE.utils.testDecodeElementText(self, self.obj,'<COMMENT>text</COMMENT>', 'comment', 'text')
        TE.utils.testDecodeElementText(self, self.obj,'<CREATION-TIME>text</CREATION-TIME>', 'creation_time', 'text')
        TE.utils.testDecodeElementText(self, self.obj,'<REPOSITORY-ID>text</REPOSITORY-ID>', 'repository_id', 'text')
        TE.utils.testDecodeElementText(self, self.obj,'<REQ-IF-TOOL-ID>text</REQ-IF-TOOL-ID>', 'req_if_tool_id', 'text')
        TE.utils.testDecodeElementText(self, self.obj,'<SOURCE-TOOL-ID>text</SOURCE-TOOL-ID>', 'source_tool_id', 'text')
        TE.utils.testDecodeElementText(self, self.obj,'<TITLE>text</TITLE>', 'title', 'text')

    def test_encode(self):
        TE.utils.testEncodeAttribute(self, self.obj, 'identifier', 'IDENTIFIER')
        TE.utils.testEncodeElementText(self, self.obj,'<COMMENT>text</COMMENT>', 'comment', 'text')
        TE.utils.testEncodeElementText(self, self.obj,'<CREATION-TIME>text</CREATION-TIME>', 'creation_time', 'text')
        TE.utils.testEncodeElementText(self, self.obj,'<REPOSITORY-ID>text</REPOSITORY-ID>', 'repository_id', 'text')
        TE.utils.testEncodeElementText(self, self.obj,'<REQ-IF-TOOL-ID>text</REQ-IF-TOOL-ID>', 'req_if_tool_id', 'text')
        TE.utils.testEncodeElementText(self, self.obj,'<SOURCE-TOOL-ID>text</SOURCE-TOOL-ID>', 'source_tool_id', 'text')
        TE.utils.testEncodeElementText(self, self.obj,'<TITLE>text</TITLE>', 'title', 'text')

if __name__ == '__main__':
    unittest.main()
