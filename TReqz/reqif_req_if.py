from  xml.etree.ElementTree import Element
import TReqz

class reqif_req_if(TReqz.reqif_object):
    req_if_header:TReqz.reqif_req_if_header=None # required
    req_if_content:TReqz.reqif_req_if_content=None # required
    lang:str=None # attribute, optional
    reqif_dict:TReqz.reqif_id_dict=None

    def __init__(self, content:Element = None, id_dict=None):
        self.name = "REQ-IF"
        if id_dict == None:
            self.reqif_dict = TReqz.reqif_id_dict()
        else:
            self.reqif_dict=id_dict
        super(reqif_req_if, self).__init__(content, self.reqif_dict)

    def decode(self, content:Element, id_dict:TReqz.reqif_id_dict={}):
        super().decode(content, id_dict)
        
        self.lang = content.get("{http://www.w3.org/XML/1998/namespace}lang")
        namespace = TReqz.reqif_utils.get_tag_namespace(content.tag)
        self.req_if_header = TReqz.reqif_utils.generate_object_by_element_class(content, id_dict, "./{0}THE-HEADER/{0}REQ-IF-HEADER".format(namespace), "reqif_req_if_header")
        self.req_if_content = TReqz.reqif_utils.generate_object_by_element_class(content, id_dict, "./{0}CORE-CONTENT/{0}REQ-IF-CONTENT".format(namespace), "reqif_req_if_content")    
    
    def encode(self):
        elem = super().encode()
        elem.tag = self.name
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns", "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd")
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns:xsi", "http://www.w3.org/2001/XMLSchema-instance")
        TReqz.reqif_utils.setElementAttribute(elem, "xsi:schemaLocation", "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd reqif.xsd")
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns:reqif", "http://www.omg.org/spec/ReqIF/20110401/reqif.xsd")
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns:reqif-xhtml", "http://www.w3.org/1999/xhtml")
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns:rm-reqif", "http://www.ibm.com/rm/reqif")
        TReqz.reqif_utils.setElementAttribute(elem, "xmlns:xhtml", "http://www.w3.org/1999/xhtml")
        
        TReqz.reqif_utils.setElementAttribute(elem, "{http://www.w3.org/XML/1998/namespace}lang", self.lang)
        headerElement = TReqz.reqif_utils.addRequiredSubElement(elem, "THE-HEADER")
        TReqz.reqif_utils.addEncodedSubElement(headerElement, self.req_if_header)
        contentElement = TReqz.reqif_utils.addRequiredSubElement(elem, "CORE-CONTENT")
        TReqz.reqif_utils.addEncodedSubElement(contentElement, self.req_if_content)
        return elem
