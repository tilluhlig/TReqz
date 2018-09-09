import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_date(TReqz.reqif_datatype_definition):
    
    def encode(self):
        elem = super().encode()
        elem.tag = "DATATYPE-DEFINITION-DATE"
        return elem