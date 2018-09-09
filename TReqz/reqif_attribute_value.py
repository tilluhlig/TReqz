from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_value(TReqz.reqif_object):
    definition:TReqz.reqif_datatype_definition=None # element, required
    the_value:str=None # attribute, required

    def __init__(self, content:Element = None, id_dict={}):
        super(reqif_attribute_value, self).__init__(content, id_dict)

    def getValues(self):
        return [self.the_value]
        
    def encode(self):
        elem = super().encode()
        return elem