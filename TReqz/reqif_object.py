from xml.etree.ElementTree import Element
import re
import TReqz


class reqif_object:
    name: str = "no name"

    def __init__(self, content: Element = None, id_dict={}):  # :TReqz.reqif_id_dict.reqif_id_dict
        if content != None:
            self.decode(content, id_dict)

    def fill(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def decode(self, content: Element, id_dict={}):  # :TReqz.reqif_id_dict.reqif_id_dict
        pass

    def encode(self):
        return TReqz.reqif_utils.createSubElement(None)
