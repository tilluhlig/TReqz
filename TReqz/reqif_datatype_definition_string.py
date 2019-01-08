from .. import TReqz
from xml.etree.ElementTree import Element


class reqif_datatype_definition_string(TReqz.reqif_datatype_definition):

    def __init__(self, content: Element = None, id_dict=None):
        self.max_length = None  # attribute, required
        self.name = "DATATYPE-DEFINITION-STRING"
        super(reqif_datatype_definition_string,
              self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = None):
        super().decode(content, id_dict)
        self.max_length = content.get("MAX-LENGTH")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.xml_utils.setElementAttribute(
            elem, "MAX-LENGTH", self.max_length)
        return elem
