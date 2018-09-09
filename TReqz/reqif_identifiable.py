import xml.etree.cElementTree as ET
from  xml.etree.ElementTree import Element
from  xml.etree.ElementTree import ElementTree
import TReqz

class reqif_identifiable(TReqz.reqif_object):
    desc:str=None # attribute, optional
    identifier:str=None # attribute, required
    last_change:str=None # attribute, required
    long_name:str=None # attribute, optional
    alternative_id:str=None # element, optional

    def create(self, id_dict={}):
        self.identifier=TReqz.reqif_utils.generateNextLocalId(id_dict)
        if self.identifier != None:
            id_dict.add(self)
        else:
            # problem
            pass
        return self.identifier

    def decode(self, content:Element, id_dict={}): #:TReqz.reqif_id_dict.reqif_id_dict
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.desc = content.get("DESC")
        self.identifier = content.get("IDENTIFIER")
        if self.identifier != None:
            id_dict.add(self)
        self.last_change = content.get("LAST-CHANGE")
        self.long_name = content.get("LONG-NAME")

        alternativeidElement = TReqz.reqif_utils.get_element(content, "./{0}ALTERNATIVE-ID/{0}ALTERNATIVE-ID".format(namespace))
        if alternativeidElement != None:
            self.alternative_id = alternativeidElement.get("IDENTIFIER")

    def encode(self):
        elem = super().encode()
        TReqz.reqif_utils.setElementAttribute(elem, "DESC", self.desc)
        TReqz.reqif_utils.setElementAttribute(elem, "IDENTIFIER", self.identifier)
        TReqz.reqif_utils.setElementAttribute(elem, "LAST-CHANGE", self.last_change)
        TReqz.reqif_utils.setElementAttribute(elem, "LONG-NAME", self.long_name)

        if self.alternative_id != None:
            alternativeidElement = TReqz.reqif_utils.addRequiredSubElement(elem, "ALTERNATIVE-ID")
            alternativeidElementWithAttribute = TReqz.reqif_utils.addRequiredSubElement(alternativeidElement, "ALTERNATIVE-ID")
            TReqz.reqif_utils.setElementAttribute(alternativeidElementWithAttribute, "IDENTIFIER", self.alternative_id)

        return elem