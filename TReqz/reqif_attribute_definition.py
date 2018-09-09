from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_definition(TReqz.reqif_identifiable):
    default_value:TReqz.reqif_attribute_value=None # element, optional
    type:TReqz.reqif_datatype_definition=None # local_ref, required
    is_editable:str=None # attribute, optional

    def __init__(self, content:Element = None, id_dict={}):
        super(reqif_attribute_definition, self).__init__(content, id_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.is_editable = content.get("IS-EDITABLE")    

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(elem, "IS-EDITABLE", self.is_editable)
        return elem
