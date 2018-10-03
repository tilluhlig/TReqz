import TReqz
from xml.etree.ElementTree import Element


class reqif_embeded_value(TReqz.reqif_object):

    def __init__(self, content: Element = None, id_dict={}):
        self.key: str = None  # attribute, required
        self.other_content: str = None  # attribute, required
        self.name = "EMBEDDED-VALUE"
        super(reqif_embeded_value, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        self.key = content.get("KEY")
        self.other_content = content.get("OTHER-CONTENT")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.xml_utils.setElementAttribute(elem, "KEY", self.key)
        TReqz.xml_utils.setElementAttribute(
            elem, "OTHER-CONTENT", self.other_content)
        return elem
