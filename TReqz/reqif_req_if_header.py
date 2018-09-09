from  xml.etree.ElementTree import Element
import TReqz

class reqif_req_if_header(TReqz.reqif_object):
    comment:str=None # element, optional
    creation_time:str=None # element, required
    repository_id:str=None # element, optional
    req_if_tool_id:str=None # element, required
    req_if_version:str="1.0" # element, required
    source_tool_id:str=None # element, required
    title:str=None # element, required
    identifier:str=None # attribute, required

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        namespace =TReqz.reqif_utils.get_tag_namespace(content.tag)

        self.identifier = content.get("IDENTIFIER")
        if self.identifier != None:
            id_dict.add(self)
        self.comment = content.findtext("./{0}COMMENT".format(namespace))
        self.creation_time = content.findtext("./{0}CREATION-TIME".format(namespace))
        self.repository_id = content.findtext("./{0}REPOSITORY-ID".format(namespace))
        self.req_if_tool_id = content.findtext("./{0}REQ-IF-TOOL-ID".format(namespace))
        self.req_if_version = content.findtext("./{0}REQ-IF-VERSION".format(namespace), "1.0")
        self.source_tool_id = content.findtext("./{0}SOURCE-TOOL-ID".format(namespace))
        self.title = content.findtext("./{0}TITLE".format(namespace))

    def encode(self):
        elem = super().encode()
        elem.tag = "REQ-IF-HEADER"
        TReqz.reqif_utils.setElementAttribute(elem, "IDENTIFIER", self.identifier)
        TReqz.reqif_utils.addOptionalSubElement(elem, "COMMENT", self.comment)
        TReqz.reqif_utils.addOptionalSubElement(elem, "CREATION-TIME", self.creation_time)
        TReqz.reqif_utils.addOptionalSubElement(elem, "REPOSITORY-ID", self.repository_id)
        TReqz.reqif_utils.addOptionalSubElement(elem, "REQ-IF-TOOL-ID", self.req_if_tool_id)
        TReqz.reqif_utils.addOptionalSubElement(elem, "REQ-IF-VERSION", self.req_if_version)
        TReqz.reqif_utils.addOptionalSubElement(elem, "SOURCE-TOOL-ID", self.source_tool_id)
        TReqz.reqif_utils.addOptionalSubElement(elem, "TITLE", self.title)
        return elem


