from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import TReqz
import re


class reqif_attribute_value_xhtml(TReqz.reqif_attribute_value):

    def __init__(self, content: Element = None, id_dict={}):
        self.definition: TReqz.reqif_attribute_definition_xhtml = None  # localRef, required
        self.the_original_value: str = None  # element, optional
        self.is_simplified: str = None  # attribute, optional
        self.name = "ATTRIBUTE-VALUE-XHTML"
        super(reqif_attribute_value_xhtml, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        elem = TReqz.reqif_utils.get_element(
            content, "./{0}THE-VALUE".format(namespace))
        if elem != None:
            all_descendants = list(elem.iter())
            all_descendants = all_descendants[1:]
            oldTag = elem.tag = None
            elem.tag = None
            for element in all_descendants:
                element.tag = re.sub(
                    r"{[\S]*}([\S]*)",
                    "\\1",
                    element.tag
                )
            self.the_value = ET.tostring(elem, encoding='utf-8', method='xml')
            self.the_value = self.the_value.decode("utf-8")
            elem.tag = oldTag
        elem = TReqz.reqif_utils.get_element(
            content, "./{0}THE-ORIGINAL-VALUE".format(namespace))
        if elem != None:
            self.the_original_value = ET.tostring(
                elem, encoding='utf-8', method='text')
        self.is_simplified = content.get("IS-SIMPLIFIED")
        self.definition = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}DEFINITION/{0}ATTRIBUTE-DEFINITION-XHTML-REF".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(
            elem, "IS-SIMPLIFIED", self.is_simplified)

        TReqz.reqif_utils.addOptionalSubElement(
            elem, "THE-ORIGINAL-VALUE", self.the_original_value)

        value = self.the_value
        if value == None or value=="":
            value =  "<p/>"

        result = ET.fromstring("<div>"+value+"</div>")

        all_descendants = list(result.iter())
        for element in all_descendants:
            element.tag = "{http://www.w3.org/1999/xhtml}"+element.tag

        thevalueElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "THE-VALUE")
        thevalueElement.append(result)

        definitionElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "DEFINITION")
        TReqz.reqif_utils.addRequiredSubElement(
            definitionElement, "ATTRIBUTE-DEFINITION-XHTML-REF", self.definition.identifier)
        return elem
