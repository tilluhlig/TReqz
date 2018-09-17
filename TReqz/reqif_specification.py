from xml.etree.ElementTree import Element
import TReqz


class reqif_specification(TReqz.reqif_identifiable):

    def __init__(self, content: Element = None, id_dict={}):
        self.values: list = list()  # reqif_attribute_value
        self.children: list = list()  # reqif_spec_hierarchy
        self.type: TReqz.reqif_specification_type = None  # localRef, required
        self.name = "SPECIFICATION"
        super(reqif_specification, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        typeList = {"ATTRIBUTE-VALUE-BOOLEAN": "reqif_attribute_value_boolean",
                    "ATTRIBUTE-VALUE-DATE": "reqif_attribute_value_date",
                    "ATTRIBUTE-VALUE-ENUMERATION": "reqif_attribute_value_enumeration",
                    "ATTRIBUTE-VALUE-INTEGER": "reqif_attribute_value_integer",
                    "ATTRIBUTE-VALUE-REAL": "reqif_attribute_value_real",
                    "ATTRIBUTE-VALUE-STRING": "reqif_attribute_value_string",
                    "ATTRIBUTE-VALUE-XHTML": "reqif_attribute_value_xhtml"}
        self.values = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}VALUES".format(namespace), typeList)

        typeList = {"SPEC-HIERARCHY": "reqif_spec_hierarchy"}
        self.children = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}CHILDREN".format(namespace), typeList)

        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TYPE/{0}SPECIFICATION-TYPE-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        if len(self.values) > 0:
            valuesElement = TReqz.reqif_utils.addRequiredSubElement(
                elem, "VALUES")
            for value in self.values:
                TReqz.reqif_utils.addEncodedSubElement(valuesElement, value)

        if len(self.children) > 0:
            childrenElement = TReqz.reqif_utils.addRequiredSubElement(
                elem, "CHILDREN")
            for child in self.children:
                TReqz.reqif_utils.addEncodedSubElement(childrenElement, child)

        typeElement = TReqz.reqif_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.reqif_utils.addRequiredSubElement(
            typeElement, "SPECIFICATION-TYPE-REF", self.type.identifier)

        return elem
