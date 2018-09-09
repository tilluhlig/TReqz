from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_value_real(TReqz.reqif_attribute_value):
    definition:TReqz.reqif_datatype_definition_real = None # localRef, required

    def __init__(self, content:Element = None, id_dict={}):
        self.name = "ATTRIBUTE-VALUE-REAL"
        super(reqif_attribute_value_real, self).__init__(content, id_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        self.the_value = content.get("THE-VALUE")
        self.definition = TReqz.reqif_utils.get_local_ref_from_element_text(content, id_dict, "./{0}DEFINITION/{0}ATTRIBUTE-DEFINITION-REAL-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(elem, "THE-VALUE", self.the_value)
        definitionElement = TReqz.reqif_utils.addRequiredSubElement(elem, "DEFINITION")
        TReqz.reqif_utils.addRequiredSubElement(definitionElement, "ATTRIBUTE-DEFINITION-REAL-REF", self.definition.identifier)
        return elem