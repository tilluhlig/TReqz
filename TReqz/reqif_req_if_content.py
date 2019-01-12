from xml.etree.ElementTree import Element
from .. import TReqz


class reqif_req_if_content(TReqz.reqif_object):

    def __init__(self, content: Element = None, id_dict=None):
        self.datatypes: list = list()  # reqif_datatype_definition, optional
        # reqif_specification_type, reqif_spec_relation_type, reqif_spec_object_type, reqif_relation_group_type, optional
        self.spec_types: list = list()
        self.spec_objects: list = list()  # reqif_spec_object, optional
        self.spec_relations: list = list()  # reqif_spec_relation, optional
        self.specifications: list = list()  # reqif_specification, optional
        self.spec_relation_groups: list = list()  # reqif_relation_group, optional
        super(reqif_req_if_content, self).__init__(content, id_dict)
        self.name = "REQ-IF-CONTENT"

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = None):
        super().decode(content, id_dict)
        namespace = TReqz.xml_utils.get_tag_namespace(content.tag)

        self.datatypes = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}DATATYPES".format(namespace), TReqz.reqif_config.DATATYPE_DEFINITION_TAG_TO_CLASS)

        self.spec_types = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPEC-TYPES".format(namespace), TReqz.reqif_config.SPEC_TYPES_TAG_TO_CLASS)

        typeList = {"SPEC-OBJECT": "reqif_spec_object"}
        self.spec_objects = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPEC-OBJECTS".format(namespace), typeList)

        typeList = {"SPEC-RELATION": "reqif_spec_relation"}
        self.spec_relations = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPEC-RELATIONS".format(namespace), typeList)

        typeList = {"SPECIFICATION": "reqif_specification"}
        self.specifications = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPECIFICATIONS".format(namespace), typeList)

        typeList = {"RELATION-GROUP": "reqif_relation_group"}
        self.spec_relation_groups = TReqz.reqif_utils.generate_object_list_by_element_class(
            content, id_dict, "./{0}SPEC-RELATION-GROUPS".format(namespace), typeList)

    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        if len(self.datatypes) > 0:
            datatypesElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "DATATYPES")
            for element in self.datatypes:
                TReqz.xml_utils.addEncodedSubElement(
                    datatypesElement, element)

        if len(self.spec_types) > 0:
            spectypesElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "SPEC-TYPES")
            for element in self.spec_types:
                TReqz.xml_utils.addEncodedSubElement(
                    spectypesElement, element)

        if len(self.spec_objects) > 0:
            specobjectsElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "SPEC-OBJECTS")
            for element in self.spec_objects:
                TReqz.xml_utils.addEncodedSubElement(
                    specobjectsElement, element)

        if len(self.spec_relations) > 0:
            specrelationsElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "SPEC-RELATIONS")
            for element in self.spec_relations:
                TReqz.xml_utils.addEncodedSubElement(
                    specrelationsElement, element)

        if len(self.specifications) > 0:
            specificationsElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "SPECIFICATIONS")
            for element in self.specifications:
                TReqz.xml_utils.addEncodedSubElement(
                    specificationsElement, element)

        if len(self.spec_relation_groups) > 0:
            specrelationgroupsElement = TReqz.xml_utils.addRequiredSubElement(
                elem, "SPEC-RELATION-GROUPS")
            for element in self.spec_relation_groups:
                TReqz.xml_utils.addEncodedSubElement(
                    specrelationgroupsElement, element)

        return elem
