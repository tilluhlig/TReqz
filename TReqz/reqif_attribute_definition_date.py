from  xml.etree.ElementTree import Element
import TReqz

class reqif_attribute_definition_date(TReqz.reqif_attribute_definition):

    def __init__(self, content:Element = None, id_dict={}):
        self.name = "ATTRIBUTE-DEFINITION-DATE"
        super(reqif_attribute_definition_date, self).__init__(content, id_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.default_value = TReqz.reqif_utils.generate_object_by_element_class(content, id_dict, "./{0}DEFAULT-VALUE".format(namespace), "reqif_attribute_value_date")

        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(content, id_dict, "./{0}TYPE/{0}DATATYPE-DEFINITION-DATE-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        if self.default_value != None:
            defaultElement = TReqz.reqif_utils.addRequiredSubElement(elem, "DEFAULT-VALUE")
            TReqz.reqif_utils.addEncodedSubElement(defaultElement, self.default_value)
        typeElement = TReqz.reqif_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.reqif_utils.addRequiredSubElement(typeElement, "DATATYPE-DEFINITION-DATE-REF", self.type.identifier)
        return elem