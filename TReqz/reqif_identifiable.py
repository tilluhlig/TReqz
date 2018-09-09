import xml.etree.cElementTree as ET
from  xml.etree.ElementTree import Element
from  xml.etree.ElementTree import ElementTree
import TReqz

class reqif_identifiable(TReqz.reqif_object):
    desc:str=None # attribute, optional
    identifier:str=None # attribute, required
    last_change:str=None # attribute, required
    long_name:str=None # attribute, optional

    def decode(self, content:Element, id_dict={}): #:TReqz.reqif_id_dict.reqif_id_dict
        super().decode(content, id_dict)
        self.desc = content.get("DESC")
        self.identifier = content.get("IDENTIFIER")
        if self.identifier != None:
            id_dict.add(self)
        self.last_change = content.get("LAST-CHANGE")
        self.long_name = content.get("LONG-NAME")

    def encode(self):
        elem = super().encode()
        TReqz.reqif_utils.setElementAttribute(elem, "DESC", self.desc)
        TReqz.reqif_utils.setElementAttribute(elem, "IDENTIFIER", self.identifier)
        TReqz.reqif_utils.setElementAttribute(elem, "LAST-CHANGE", self.last_change)
        TReqz.reqif_utils.setElementAttribute(elem, "LONG-NAME", self.long_name)
        return elem