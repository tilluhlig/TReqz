from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_value(TReqz.reqif_object):
    definition:TReqz.reqif_datatype_definition=None # element, required

    def encode(self):
        elem = super().encode()
        return elem