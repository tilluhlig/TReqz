from xml.etree.ElementTree import Element
import re
import TReqz


class reqif_object(TReqz.xml_object):

    def __init__(self, content: Element = None, id_dict={}):  # :TReqz.reqif_id_dict.reqif_id_dict
        if content != None:
            self.decode(content, id_dict)

    def decode(self, content: Element, id_dict={}):  # :TReqz.reqif_id_dict.reqif_id_dict
        pass
