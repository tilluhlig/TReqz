import TReqz
from  xml.etree.ElementTree import Element

class reqif_datatype_definition_enumeration(TReqz.reqif_datatype_definition):
    specified_values:list = list() # reqif_enum_value, element, optional

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        elem:Element = content.find("./{0}SPECIFIED-VALUES".format(namespace))
        self.specified_values:list = list()
        if elem != None:
            valueElements = list(elem)
            for elem in valueElements:
                newElem = TReqz.reqif_enum_value(elem, id_dict)
                self.specified_values.append(newElem)    

    def encode(self):
        elem = super().encode()
        elem.tag = "DATATYPE-DEFINITION-ENUMERATION"
        if len(self.specified_values)>0:
            valuesElement = TReqz.reqif_utils.addRequiredSubElement(elem, "SPECIFIED-VALUES")
            for value in self.specified_values:
                TReqz.reqif_utils.addEncodedSubElement(valuesElement, value)
        return elem