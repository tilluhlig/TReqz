import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_real(TReqz.reqif_datatype_definition):
    accuracy:int=None # attribute, required
    max:int=None # attribute, required
    min:int=None # attribute, required

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        self.accuracy = content.get("ACCURACY")
        self.max = content.get("MAX")
        self.min = content.get("MIN")
        
    def encode(self):
        elem = super().encode()
        elem.tag = "DATATYPE-DEFINITION-REAL"
        TReqz.reqif_utils.setElementAttribute(elem, "ACCURACY", self.accuracy)
        TReqz.reqif_utils.setElementAttribute(elem, "MAX", self.max)
        TReqz.reqif_utils.setElementAttribute(elem, "MIN", self.min)
        return elem