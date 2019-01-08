from xml.etree.ElementTree import Element
from .. import TReqz


class reqif_attribute_value_string(TReqz.reqif_attribute_value):

    def __init__(self, content: Element = None, id_dict=None):
        self.definition: TReqz.reqif_attribute_definition_string = None  # localRef, required
        self.name = "ATTRIBUTE-VALUE-STRING"
        super(reqif_attribute_value_string, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = None):
        super().decode(content, id_dict)
        namespace = TReqz.xml_utils.get_tag_namespace(content.tag)
        self.the_value = content.get("THE-VALUE")
        self.definition = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}DEFINITION/{0}ATTRIBUTE-DEFINITION-STRING-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.xml_utils.setElementAttribute(
            elem, "THE-VALUE", self.the_value)
        definitionElement = TReqz.xml_utils.addRequiredSubElement(
            elem, "DEFINITION")
        TReqz.xml_utils.addRequiredSubElement(
            definitionElement, "ATTRIBUTE-DEFINITION-STRING-REF", self.definition.identifier)
        return elem
