from xml.etree.ElementTree import Element
import TReqz


class reqif_spec_object(TReqz.reqif_identifiable):

    def __init__(self, content: Element = None, id_dict={}):
        self.values: list = list()  # reqif_attribute_value, optional
        self.type: TReqz.reqif_spec_object_type = None  # local ref, required
        self.name = "SPEC-OBJECT"
        super(reqif_spec_object, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TYPE/{0}SPEC-OBJECT-TYPE-REF".format(namespace))

        typeList = {"ATTRIBUTE-VALUE-BOOLEAN": "reqif_attribute_value_boolean",
                    "ATTRIBUTE-VALUE-DATE": "reqif_attribute_value_date",
                    "ATTRIBUTE-VALUE-INTEGER": "reqif_attribute_value_integer",
                    "ATTRIBUTE-VALUE-ENUMERATION": "reqif_attribute_value_enumeration",
                    "ATTRIBUTE-VALUE-REAL": "reqif_attribute_value_real",
                    "ATTRIBUTE-VALUE-STRING": "reqif_attribute_value_string",
                    "ATTRIBUTE-VALUE-XHTML": "reqif_attribute_value_xhtml"}
        self.values = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}VALUES".format(namespace), typeList)

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        if len(self.values) > 0:
            valuesElement = TReqz.reqif_utils.addRequiredSubElement(
                elem, "VALUES")
            for value in self.values:
                if not value.isEmpty():
                    TReqz.reqif_utils.addEncodedSubElement(valuesElement, value)

        typeElement = TReqz.reqif_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.reqif_utils.addRequiredSubElement(
            typeElement, "SPEC-OBJECT-TYPE-REF", self.type.identifier)

        return elem
