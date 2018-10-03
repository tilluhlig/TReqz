from xml.etree.ElementTree import Element
import TReqz


class reqif_spec_relation(TReqz.reqif_identifiable):

    def __init__(self, content: Element = None, id_dict={}):
        self.values: list()  # reqif_attribute_value, optional
        self.source: TReqz.reqif_object  # local_ref, required
        self.target: TReqz.reqif_object  # local_ref, required
        self.type: TReqz.reqif_spec_relation_type  # local_ref, required
        self.name = "SPEC-RELATION"
        super(reqif_spec_relation, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.xml_utils.get_tag_namespace(content.tag)

        typeList = {"ATTRIBUTE-VALUE-BOOLEAN": "reqif_attribute_value_boolean",
                    "ATTRIBUTE-VALUE-DATE": "reqif_attribute_value_date",
                    "ATTRIBUTE-VALUE-ENUMERATION": "reqif_attribute_value_enumeration",
                    "ATTRIBUTE-VALUE-INTEGER": "reqif_attribute_value_integer",
                    "ATTRIBUTE-VALUE-REAL": "reqif_attribute_value_real",
                    "ATTRIBUTE-VALUE-STRING": "reqif_attribute_value_string",
                    "ATTRIBUTE-VALUE-XHTML": "reqif_attribute_value_xhtml"}
        self.values = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}VALUES".format(namespace), typeList)

        self.source = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}SOURCE")
        self.target = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TARGET")
        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TYPE")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        if len(self.values) > 0:
            valuesElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "VALUES")
            for value in self.values:
                TReqz.xml_utils.addEncodedSubElement(valuesElement, value)

        typeElement = TReqz.xml_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.xml_utils.addRequiredSubElement(
            typeElement, "SPEC-RELATION-TYPE-REF", self.type.identifier)

        sourceElement = TReqz.xml_utils.addRequiredSubElement(elem, "SOURCE")
        TReqz.xml_utils.addRequiredSubElement(
            sourceElement, "SPEC-OBJECT-REF", self.source.identifier)

        targetElement = TReqz.xml_utils.addRequiredSubElement(elem, "TARGET")
        TReqz.xml_utils.addRequiredSubElement(
            targetElement, "SPEC-OBJECT-REF", self.target.identifier)

        return elem
