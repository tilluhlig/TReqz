from  xml.etree.ElementTree import Element
import TReqz

class reqif_spec_hierarchy(TReqz.reqif_identifiable):
    children:list=list() # reqif_spec_hierarchy
    req_object:TReqz.reqif_object # local_ref, required
    editable_atts:list=list() # optional  TODO TODO
    is_editable:str=None # attribute, optional
    is_table_internal:str=None # attribute, optional

    def __init__(self, content:Element = None, id_dict={}):
        self.name = "SPEC-HIERARCHY"
        super(reqif_spec_hierarchy, self).__init__(content, id_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        self.req_object = TReqz.reqif_utils.get_local_ref_from_element_text(content, id_dict, "./{0}OBJECT/{0}SPEC-OBJECT-REF".format(namespace)) 
 
        typeList = {"SPEC-HIERARCHY": "reqif_spec_hierarchy"}
        self.children = TReqz.reqif_utils.generate_object_list_by_element_class(content, id_dict, "./{0}CHILDREN".format(namespace), typeList)

        self.editable_atts = TReqz.reqif_utils.generate_local_ref_list_from_elements_text(content, id_dict, "./{0}EDITABLE-ATTS")    

        self.is_editable = content.get("IS-EDITABLE")
        self.is_table_internal = content.get("IS-TABLE-INTERNAL")

    def encode(self):
        elem = super().encode()
        elem.tag = self.name

        if len(self.children)>0:
            childrenElement = TReqz.reqif_utils.addRequiredSubElement(elem, "CHILDREN")
            for child in self.children:
                TReqz.reqif_utils.addEncodedSubElement(childrenElement, child)

        if len(self.editable_atts)>0:
            attsElement = TReqz.reqif_utils.addRequiredSubElement(elem, "EDITABLE-ATTS")
            for attribute in self.editable_atts:
                TReqz.reqif_utils.addRequiredSubElement(attsElement, attribute.name+"-REF", attribute.identifier)

        objectElement = TReqz.reqif_utils.addRequiredSubElement(elem, "OBJECT")
        TReqz.reqif_utils.addRequiredSubElement(objectElement, "SPEC-OBJECT-REF", self.req_object.identifier)

        TReqz.reqif_utils.setElementAttribute(elem, "IS-EDITABLE", self.is_editable)
        TReqz.reqif_utils.setElementAttribute(elem, "IS-TABLE-INTERNAL", self.is_table_internal)
        return elem



