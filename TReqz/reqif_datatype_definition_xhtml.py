import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_xhtml(TReqz.reqif_datatype_definition):

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)

    def encode(self):
        elem = super().encode()
        elem.tag = "DATATYPE-DEFINITION-XHTML"
        return elem

