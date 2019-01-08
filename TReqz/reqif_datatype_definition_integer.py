from .. import TReqz
from xml.etree.ElementTree import Element


class reqif_datatype_definition_integer(TReqz.reqif_datatype_definition):

    def __init__(self, content: Element = None, id_dict=None):
        self.max: int = None  # attribute, required
        self.min: int = None  # attribute, required
        self.name = "DATATYPE-DEFINITION-INTEGER"
        super(reqif_datatype_definition_integer,
              self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = None):
        super().decode(content, id_dict)
        self.max = content.get("MAX")
        self.min = content.get("MIN")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.xml_utils.setElementAttribute(elem, "MAX", self.max)
        TReqz.xml_utils.setElementAttribute(elem, "MIN", self.min)
        return elem
