
class reqif_config:

    REQIF_NAMESPACE = "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd"

    ATTRIBUTE_DEFINITION_TO_VALUE: dict() = {"reqif_attribute_definition_boolean": "reqif_attribute_value_boolean",
                                             "reqif_attribute_definition_date": "reqif_attribute_value_date",
                                             "reqif_attribute_definition_enumeration": "reqif_attribute_value_enumeration",
                                             "reqif_attribute_definition_integer": "reqif_attribute_value_integer",
                                             "reqif_attribute_definition_real": "reqif_attribute_value_real",
                                             "reqif_attribute_definition_string": "reqif_attribute_value_string",
                                             "reqif_attribute_definition_xhtml": "reqif_attribute_value_xhtml"}

    ATTRIBUTE_VALUE_TO_DEFINITION = dict(
        map(reversed, ATTRIBUTE_DEFINITION_TO_VALUE.items()))

    ATTRIBUTE_DEFINITION_TAG_TO_CLASS = {"ATTRIBUTE-DEFINITION-BOOLEAN": "reqif_attribute_definition_boolean",
                                         "ATTRIBUTE-DEFINITION-DATE": "reqif_attribute_definition_date",
                                         "ATTRIBUTE-DEFINITION-INTEGER": "reqif_attribute_definition_integer",
                                         "ATTRIBUTE-DEFINITION-ENUMERATION": "reqif_attribute_definition_enumeration",
                                         "ATTRIBUTE-DEFINITION-REAL": "reqif_attribute_definition_real",
                                         "ATTRIBUTE-DEFINITION-STRING": "reqif_attribute_definition_string",
                                         "ATTRIBUTE-DEFINITION-XHTML": "reqif_attribute_definition_xhtml"}
