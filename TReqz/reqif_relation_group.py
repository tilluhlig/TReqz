from xml.etree.ElementTree import Element
import TReqz


class reqif_relation_group(TReqz.reqif_identifiable):

    def __init__(self, content: Element = None, id_dict={}):
        self.source_specification: TReqz.reqif_object  # local_ref, required
        self.target_specification: TReqz.reqif_object  # local_ref, required
        self.spec_relations: list = list()  # local_ref, optional
        self.type: TReqz.reqif_relation_group_type  # local_ref, required
        self.name = "RELATION_GROUP"
        super(reqif_relation_group, self).__init__(content, id_dict)

    def decode(self, content: Element, id_dict: TReqz.reqif_id_dict = {}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.source_specification = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}SOURCE-SPECIFICATION")
        self.target_specification = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TARGET-SPECIFICATION")
        self.type = TReqz.reqif_utils.get_local_ref_from_element_text(
            content, id_dict, "./{0}TYPE")
        self.spec_relations = TReqz.reqif_utils.generate_local_ref_list_from_elements_text(
            content, id_dict, "./{0}SPEC-RELATIONS".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        typeElement = TReqz.reqif_utils.addRequiredSubElement(elem, "TYPE")
        TReqz.reqif_utils.addRequiredSubElement(
            typeElement, "RELATION-GROUP-TYPE-REF", self.type.identifier)

        sourceElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "SOURCE-SPECIFICATION")
        TReqz.reqif_utils.addRequiredSubElement(
            sourceElement, "SPECIFICATION-REF", self.source_specification.identifier)

        targetElement = TReqz.reqif_utils.addRequiredSubElement(
            elem, "TARGET-SPECIFICATION")
        TReqz.reqif_utils.addRequiredSubElement(
            targetElement, "SPECIFICATION-", self.target_specification.identifier)

        if len(self.spec_relations) > 0:
            attsElement = TReqz.reqif_utils.addRequiredSubElement(
                elem, "SPEC-RELATIONS")
            for spec in self.spec_relations:
                TReqz.reqif_utils.addRequiredSubElement(
                    attsElement, "SPEC-RELATION-REF", spec.identifier)

        return elem
