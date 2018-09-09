import TReqz
from  xml.etree.ElementTree import Element

class reqif_embeded_value(TReqz.reqif_object):
    key:str=None # attribute, required
    other_content:str=None # attribute, required

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        self.key = content.get("KEY")
        self.other_content = content.get("OTHER-CONTENT")

    def encode(self):
        elem = super().encode()
        elem.tag = "EMBEDDED-VALUE"
        TReqz.reqif_utils.setElementAttribute(elem, "KEY", self.key)
        TReqz.reqif_utils.setElementAttribute(elem, "OTHER-CONTENT", self.other_content)
        return elem