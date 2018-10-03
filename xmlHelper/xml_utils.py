from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
import xml.etree.ElementTree as ET
import re
import io
import hashlib
import xmlHelper
import datetime
import pytz
from lxml import etree


class xml_utils:
    """ this class contains useful xml functions
    """

    @staticmethod
    def check_tag_name(tag: str, expectedName: str):
        """ compares a tag with an expected tag-name (expectedName)

        Arguments:
            tag {str} -- a tag like "{ns}DIV"
            expectedName {str} -- a expected tag-name like "DIV"

        Returns:
            {bool} -- whether the tag name is the expected (true = yes, false = no)
        """

        return xml_utils.get_tag_name(tag) == expectedName

    @staticmethod
    def get_tag_name(tag: str):
        """ removes the leading namespace from a tag

        Arguments:
            tag {str} -- the tag

        Returns:
            [type] -- the converted tag without its namespace
        """

        name = re.split("\{.*\}", tag)
        if len(name)>=2:
            return name[1]
        return tag

    @staticmethod
    def get_tag_namespace(tag: str):
        """ extracts the namespace from a tag

        Arguments:
            tag {str} -- the tag

        Returns:
            {str} -- the namespace
        """

        namespace = re.match("\{.*\}", tag)
        if namespace != None:
            return namespace.group(0)
        return ""

    @staticmethod
    def get_text_from_element(content: Element, element_path: str):
        """ extracts the element text

        Arguments:
            content {Element} -- the root element
            element_path {str} -- the requested element

        Returns:
            {str} -- the text
        """

        elem: Element = content.find(element_path)
        if elem == None:
            return None
        return elem.text

    @staticmethod
    def get_element(content: Element, element_path: str):
        """ returns an element which is located on element_path

        Arguments:
            content {Element} -- the root element
            element_path {str} -- the requested path

        Returns:
            {Element} -- the Element
        """

        elem: Element = content.find(element_path)
        return elem

    @staticmethod
    def current_timestamp():
        """ returns the current timestamp

        Returns:
            {str} -- the timestamp
        """
        return datetime.datetime.now(pytz.utc).isoformat()

    @staticmethod
    def merge_elements(target: Element, source: Element):
        """ merges two elements

        Arguments:
            target {Element} -- the target element
            source {Element} -- the source element
        """

        # the target-dictionary is dominant

        # merge attributes
        if (target.attrib == None):
            target.attrib = {}
        if (source.attrib == None):
            source.attrib = {}
        td: dict = target.attrib
        sd: dict = source.attrib
        for key, value in sd.items():
            if td.get(key) == None:
                td[key] = value
            else:
                # the key already exists
                pass

        # merge elements
        # todo: recursive merge
        for elem in source.iter():
            target.append(elem)

    @staticmethod
    def setElementAttribute(elem: Element, attribute: str, value: str):
        """ sets an element attribute

        Arguments:
            elem {Element} -- the element
            attribute {str} -- the attribute name
            value {str} -- the new value
        """

        if value != None:
            elem.set(attribute, value)

    @staticmethod
    def createSubElement(name: str, content: str = None):
        """ creates a new element

        Arguments:
            name {str} -- the tag-name

        Keyword Arguments:
            content {str} -- an optional content (default: {None})

        Returns:
            {Element} -- the new Element
        """

        newElem = Element(name)
        if content != None:
            newElem.text = content
        return newElem

    @staticmethod
    def addRequiredSubElement(elem: Element, name: str, content: str = None):
        """ ads+creates a required element to an element (elem)

        Arguments:
            elem {Element} -- the parent element
            name {str} -- the name of the new sub-element

        Keyword Arguments:
            content {str} -- a optional content for the sub-element (default: {None})

        Returns:
            {Element} -- the new sub-element
        """

        newElem = xmlHelper.xml_utils.createSubElement(name, content)
        elem.append(newElem)
        return newElem

    @staticmethod
    def addOptionalSubElement(elem: Element, name: str, content: str = ""):
        """ adds+creates an optional element to an element (elem).
            the element would be added if the content is not None

        Arguments:
            elem {Element} -- the parent element
            name {str} -- the name of the new sub-element

        Keyword Arguments:
            content {str} -- a optional content for the sub-element (default: {None})

        Returns:
            {Element} -- the new sub-element
        """

        if content != None:
            newElem = xmlHelper.xml_utils.createSubElement(name, content)
            elem.append(newElem)
            return newElem
        return None

    @staticmethod
    def addEncodedSubElement(elem: Element, subElem):
        """ adds an element (subElem) to elem and encodes subElem (from reqif)

        Arguments:
            elem {Element} -- the parent element
            subElem {reqif_} -- the new sub-element (which needs to be encoded from reqif)

        Returns:
            {Element/None} -- the new element or None
        """

        if subElem != None:
            newElem = subElem.encode()
            elem.append(newElem)
            return newElem
        return None

    @staticmethod
    def generateMd5(content: str):
        """ generates a md5 hash for the given <content>

        Arguments:
            content {str} -- the content

        Returns:
            {str} -- a hex representation of the md5 hash
        """

        m = hashlib.md5()
        m.update(content.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def validateXmlFile(filePath:str, schemaPath:str)->bool:
        """ validates a xml-file <filePath> with a given xml-Schema (schemaPath)
        
        Arguments:
            filePath {str} -- the xml-file which needs to be validated
            schemaPath {str} -- a xml-schema
        
        Returns:
            bool -- true = is valid, false = is not valid
        """

        schemaFile = open(schemaPath,"rb")
        xmlSchemaContent:str = schemaFile.read()
        schemaFile.close()

        xmlFile = open(filePath,"rb")
        xmlFileContent:str = xmlFile.read()
        xmlFile.close()

        schema = io.BytesIO(xmlSchemaContent)
        xmlschema_doc = etree.parse(schema)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xmlFile = io.BytesIO(xmlFileContent)
        doc:ElementTree = etree.parse(xmlFile)
        res = xmlschema.validate(doc)
        error = xmlschema.error_log
        if len(error)>0:
            print(error)
        return res

    @staticmethod
    def decodeXhtml(content:Element)->str:
        """ decodes a xml represented text to string
        
        Arguments:
            content {Element} -- the xml structure
        
        Returns:
            str -- the string representation
        """

        if content != None:
            all_descendants = list(content.iter())
            all_descendants = all_descendants[1:]
            oldTag = content.tag
            content.tag = None
            for element in all_descendants:
                element.tag = re.sub(
                    r"{[\S]*}([\S]*)",
                    "\\1",
                    element.tag
                )
            value = ET.tostring(content, encoding='utf-8', method='xml')
            value = value.decode("utf-8")
            content.tag = oldTag
            return value
        return ""

    @staticmethod
    def encodeXhtml(content:str)->Element:
        """ encodes a xml string to a xml structure
        
        Arguments:
            content {str} -- the string representation
        
        Returns:
            Element -- the xml structure
        """

        if content == None or content=="":
            content =  "<p/>"

        if not xml_utils.stringIsWellFormedXml(content):
            content = "<div>"+content+"</div>"
        result = ET.fromstring(content)

        all_descendants = list(result.iter())
        for element in all_descendants:
            element.tag = "{http://www.w3.org/1999/xhtml}"+element.tag
        return element

    @staticmethod
    def stringIsWellFormedXml(content: str):
        """ checks if <content> is well formed xml

        Returns:
            {dict<bool>} -- true = is well formed, false = is not well formed
        """

        try:
            ET.fromstring(content)
        except:
            return False
        return True

    @staticmethod
    def normalizeXhtml( content: str)->str:
        """ generates a normalized form of a xhtml content.
            caution: with information loss        

        Arguments:
            content {str} -- the xhtml content

        Returns:
            str -- the normalized string
        """

        normalizedcontent = re.sub(
            r"<[^<]+>",
            "",
            content
        )
        normalizedcontent= normalizedcontent.replace("\n", "")
        return normalizedcontent