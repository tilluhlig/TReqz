import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_integer(TReqz.reqif_datatype_definition):
    max:int=None # attribute, required
    min:int=None # attribute, required

    def __init__(self, content:Element = None, id_dict={}):
        self.name = "DATATYPE-DEFINITION-INTEGER"
        super(reqif_datatype_definition_integer, self).__init__(content, id_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        self.max = content.get("MAX")
        self.min = content.get("MIN")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(elem, "MAX", self.max)
        TReqz.reqif_utils.setElementAttribute(elem, "MIN", self.min)
        return elem


