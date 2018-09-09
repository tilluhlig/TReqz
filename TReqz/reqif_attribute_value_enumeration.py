from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_value_enumeration(TReqz.reqif_attribute_value):
    definition:TReqz.reqif_datatype_definition_enumeration = None # localRef, required
    values:list=list() # localRef, reqif_enum_value, element, optional

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        self.values = TReqz.reqif_utils.generate_local_ref_list_from_elements_text(content, id_dict, "./{0}VALUES".format(namespace))
        self.definition = TReqz.reqif_utils.get_local_ref_from_element_text(content, id_dict, "./{0}DEFINITION/{0}ATTRIBUTE-DEFINITION-ENUMERATION-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = "ATTRIBUTE-VALUE-ENUMERATION"

        valuesElement = TReqz.reqif_utils.addOptionalSubElement(elem, "VALUES")
        if valuesElement != None and len(self.values)>0:
            for value in self.values:
                TReqz.reqif_utils.addRequiredSubElement(valuesElement, "ENUM-VALUE-REF", value.identifier)

        definitionElement = TReqz.reqif_utils.addRequiredSubElement(elem, "DEFINITION")
        TReqz.reqif_utils.addRequiredSubElement(definitionElement, "ATTRIBUTE-DEFINITION-ENUMERATION-REF", self.definition.identifier)
        return elem
