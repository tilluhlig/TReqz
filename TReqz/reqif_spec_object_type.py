from xml.etree.ElementTree import Element
import TReqz


class reqif_spec_object_type(TReqz.reqif_identifiable):

    def __init__(self, content: Element = None, id_dict={}):
        self.spec_attributes: list = list()  # reqif_attribute_definition, optional
        self.name = "SPEC-OBJECT-TYPE"
        super(reqif_spec_object_type, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        typeList = {"ATTRIBUTE-DEFINITION-BOOLEAN": "reqif_attribute_definition_boolean",
                    "ATTRIBUTE-DEFINITION-DATE": "reqif_attribute_definition_date",
                    "ATTRIBUTE-DEFINITION-INTEGER": "reqif_attribute_definition_integer",
                    "ATTRIBUTE-DEFINITION-ENUMERATION": "reqif_attribute_definition_enumeration",
                    "ATTRIBUTE-DEFINITION-REAL": "reqif_attribute_definition_real",
                    "ATTRIBUTE-DEFINITION-STRING": "reqif_attribute_definition_string",
                    "ATTRIBUTE-DEFINITION-XHTML": "reqif_attribute_definition_xhtml"}
        self.spec_attributes = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPEC-ATTRIBUTES".format(namespace), typeList)

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        if len(self.spec_attributes) > 0:
            specattributesElement = TReqz.reqif_utils.addRequiredSubElement(
                elem, "SPEC-ATTRIBUTES")
            for spec in self.spec_attributes:
                TReqz.reqif_utils.addEncodedSubElement(
                    specattributesElement, spec)

        return elem
