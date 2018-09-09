import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_integer(TReqz.reqif_datatype_definition):
    max:int=None # attribute, required
    min:int=None # attribute, required

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        self.max = content.get("MAX")
        self.min = content.get("MIN")

    def encode(self):
        elem = super().encode()
        elem.tag = "DATATYPE-DEFINITION-INTEGER"
        TReqz.reqif_utils.setElementAttribute(elem, "MAX", self.max)
        TReqz.reqif_utils.setElementAttribute(elem, "MIN", self.min)
        return elem


