from xml.etree.ElementTree import Element
import TReqz
import TReqz.reqif_utils


class reqif_attribute_value_enumeration(TReqz.reqif_attribute_value):

    def __init__(self, content: Element = None, id_dict={}):
        self.definition: TReqz.reqif_attribute_definition_enumeration = None  # localRef, required
        self.values: list = list()  # localRef, reqif_enum_value, element, optional
        self.name = "ATTRIBUTE-VALUE-ENUMERATION"
        super(reqif_attribute_value_enumeration,
              self).__init__(content, id_dict)

    def getValue(self):
        if len(self.values)==0 and self.definition.default_value != None:
            return [self.definition.default_value]

        returnValues = list()
        for value in self.values:
            returnValues.append(value.embedded_value.key)
        return returnValues

    def setValue(self, values: list, id_dict: TReqz.reqif_id_dict):
        if values == None:
            self.values = list()
            return

        newValues = list()
        possibleValues = self.definition.getValueMapWithEnumObjects()
        for value in values:
            possibleValue = possibleValues.get(value)
            if possibleValue == None:
                raise RuntimeError
            newValues.append(possibleValue)
        self.values = newValues

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        self.values = TReqz.reqif_utils.generate_local_ref_list_from_elements_text(
            content, id_dict, "./{0}VALUES".format(namespace))
        self.definition = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}DEFINITION/{0}ATTRIBUTE-DEFINITION-ENUMERATION-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        valuesElement = TReqz.reqif_utils.addOptionalSubElement(elem, "VALUES")
        if valuesElement != None and len(self.values) > 0:
            for value in self.values:
                TReqz.reqif_utils.addRequiredSubElement(
                    valuesElement, "ENUM-VALUE-REF", value.identifier)

        definitionElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "DEFINITION")
        TReqz.reqif_utils.addRequiredSubElement(
            definitionElement, "ATTRIBUTE-DEFINITION-ENUMERATION-REF", self.definition.identifier)
        return elem
