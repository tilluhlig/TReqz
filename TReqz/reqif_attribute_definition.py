from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_definition(TReqz.reqif_identifiable):
    default_value:TReqz.reqif_attribute_value=None # element, optional
    type:TReqz.reqif_datatype_definition=None # local_ref, required
    is_editable:str=None # attribute, optional

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.is_editable = content.get("IS-EDITABLE")    

    def encode(self):
        elem = super().encode()
        elem.tag = "ATTRIBUTE-DEFINITION"
        TReqz.reqif_utils.setElementAttribute(elem, "IS-EDITABLE", self.is_editable)
        return elem
