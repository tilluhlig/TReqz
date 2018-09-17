from xml.etree.ElementTree import Element
import TReqz


class reqif_attribute_definition_enumeration(TReqz.reqif_attribute_definition):

    def __init__(self, content: Element = None, id_dict={}):
        self.multi_valued: str = None  # attribute, required
        self.name = "ATTRIBUTE-DEFINITION-ENUMERATION"
        super(reqif_attribute_definition_enumeration,
              self).__init__(content, id_dict)

    def getValueMap(self):
        valueDefinitions = self.type.specified_values
        valueMap = dict()
        for possibleValues in valueDefinitions:
            valueMap[possibleValues.embedded_value.key] = possibleValues.long_name
        return valueMap

    def getReversedValueMap(self):
        valueMap = self.getValueMap()
        reversedValueMap = dict(
            map(reversed, valueMap.items()))
        return reversedValueMap

    def getValueMapWithEnumObjects(self):
        valueDefinitions = self.type.specified_values
        valueMap = dict()
        for possibleValues in valueDefinitions:
            valueMap[possibleValues.embedded_value.key] = possibleValues
        return valueMap

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        typeList = {
            "ATTRIBUTE-VALUE-ENUMERATION": "reqif_attribute_value_enumeration"}
        self.default_value = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}DEFAULT-VALUE".format(namespace), typeList)

        self.multi_valued = content.get("MULTI-VALUED")
        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TYPE/{0}DATATYPE-DEFINITION-ENUMERATION-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(
            elem, "MULTI-VALUED", self.multi_valued)

        defaultElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "DEFAULT-VALUE")
        if defaultElement != None and self.default_value != None:
            for value in self.default_value:
                TReqz.reqif_utils.addEncodedSubElement(defaultElement, value)

        typeElement = TReqz.reqif_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.reqif_utils.addRequiredSubElement(
            typeElement, "DATATYPE-DEFINITION-ENUMERATION-REF", self.type.identifier)
        return elem
