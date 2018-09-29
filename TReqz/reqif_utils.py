from xml.etree.ElementTree import Element
import re
import hashlib
import TReqz
import datetime
import pytz


class reqif_utils:
    @staticmethod
    def check_tag_name(tag: str, expectedName: str):
        """ compares a tag with an expected tag-name (expectedName)

        Arguments:
            tag {str} -- a tag like "{ns}DIV"
            expectedName {str} -- a expected tag-name like "DIV"

        Returns:
            {bool} -- whether the tag name is the expected (true = yes, false = no)
        """

        return reqif_utils.get_tag_name(tag) == expectedName

    @staticmethod
    def get_tag_name(tag: str):
        """ removes the leading namespace from a tag

        Arguments:
            tag {str} -- the tag

        Returns:
            [type] -- the converted tag without its namespace
        """

        name = re.split("\{.*\}", tag)
        return name[1] if name else ''

    @staticmethod
    def get_tag_namespace(tag: str):
        """ extracts the namespace from a tag

        Arguments:
            tag {str} -- the tag

        Returns:
            {str} -- the namespace
        """

        namespace = re.match("\{.*\}", tag)
        return namespace.group(0) if namespace else ''

    @staticmethod
    def generate_local_ref_list_from_elements(content: Element, id_dict: TReqz.reqif_id_dict, elements_parent_path: str):
        """ creates a list of objects which is based on refs.
            the refs are extracted from the parent_element

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dictionary
            elements_parent_path {str} -- the relative path (from content-element) where the refs are located

        Returns:
            {list<reqif_object>} -- the objects
        """

        elem: Element = content.find(elements_parent_path)
        id_list = list()
        if elem != None:
            valueElements = list(elem)
            for elem2 in valueElements:
                id_list.append(id_dict.get(elem2))
        return id_list

    @staticmethod
    def generate_local_ref_list_from_elements_text(content: Element, id_dict: TReqz.reqif_id_dict, elements_parent_path: str):
        """ creates a list of objects which is based on refs.
            the refs are extracted from the parent_element

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dictionary
            elements_parent_path {str} -- the relative path (from content-element) where the refs are located

        Returns:
            {list<reqif_object>} -- the objects
        """

        elem: Element = content.find(elements_parent_path)
        id_list = list()
        if elem != None:
            valueElements = list(elem)
            for elem2 in valueElements:
                id_list.append(id_dict.get(elem2.text))
        return id_list

    @staticmethod
    def get_local_ref_from_element(content: Element, id_dict: TReqz.reqif_id_dict, element_path: str):
        """ returns the referenced object of an element (element_path)

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dict
            element_path {str} -- the relative element path

        Returns:
            {reqif_identifiable} -- the object or None
        """

        elem: Element = content.find(element_path)
        referenced_object = id_dict.get(elem.get("IDENTIFIER"))

        if referenced_object == None:
            print("missing local ref: "+elem.get("IDENTIFIER"))
            return None

        return referenced_object

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
    def get_local_ref_from_element_text(content: Element, id_dict: TReqz.reqif_id_dict, element_path: str):
        """ returns the referenced object of an element (element_path)

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dict
            element_path {str} -- the relative element path

        Returns:
            {reqif_identifiable} -- the object or None
        """

        elem: Element = content.find(element_path)

        if elem == None:
            print("can't find the parent: "+element_path)
            return None

        id = id_dict.get(elem.text)

        if id == None:
            print("missing local ref: "+elem.text)
            return None

        return id

    @staticmethod
    def generate_object_list_by_element_class(content: Element, id_dict: TReqz.reqif_id_dict, elements_parent_path: str, typeList: dict):
        """ generates a bulk of objects by a list of possible object classes (the keys are the tags which are mapped to classes)

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dict
            elements_parent_path {str} -- the element path
            typeList {dict} -- the tag->class dict

        Returns:
            {list<reqif_>} -- the objects
        """

        elem: Element = content.find(elements_parent_path)

        if elem == None:
            return list()

        results = list()
        if elem != None:
            valueElements = elem.getchildren()
            for elem2 in valueElements:
                elemName = reqif_utils.get_tag_name(elem2.tag)
                elemClass = typeList.get(elemName)
                if elemClass != None:
                    classname = "TReqz."+elemClass
                    #typeClass = importlib.import_module(elemClass)
                    #classname = getattr(typeClass, elemClass)
                    #newObject = classname(elem2, id_dict)
                    newObject = eval(classname)(elem2, id_dict)
                    results.append(newObject)
                else:
                    # unknown type
                    pass
        return results

    @staticmethod
    def current_timestamp():
        """ returns the current timestamp

        Returns:
            {str} -- the timestamp
        """
        return datetime.datetime.now(pytz.utc).isoformat()

    @staticmethod
    def create_object_by_element_class(type: str, id_dict: TReqz.reqif_id_dict = None):
        """ creates a new object based on an class name (type)

        Arguments:
            id_dict {TReqz.reqif_id_dict} -- the id dict
            type {str} -- the class name

        Returns:
            {reqif_/None} -- the object or None
        """

        if type != None:
            classname = "TReqz."+type
            newObject = eval(classname)(None, id_dict)

            if id_dict != None and hasattr(newObject, "create"):
                newObject.create(id_dict)
            return newObject
        return None

    @staticmethod
    def generate_object_by_element_class(content: Element, id_dict: TReqz.reqif_id_dict, element_path: str, type: str):
        """ creates a new object based on an class name (type)

        Arguments:
            content {Element} -- the root element
            id_dict {TReqz.reqif_id_dict} -- the id dict
            element_path {str} -- the element path
            type {str} -- the class name

        Returns:
            {reqif_/None} -- the object or None
        """

        elem: Element = content.find(element_path)
        if type != None and elem != None:
            classname = "TReqz."+type
            #typeClass = importlib.import_module(type, 'TReqz.'+type)
            #classname = getattr(typeClass, type)
            #newObject = classname(elem, id_dict)
            newObject = eval(classname)(elem, id_dict)
            return newObject
        return None

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

        newElem = TReqz.reqif_utils.createSubElement(name, content)
        elem.append(newElem)
        return newElem

    @staticmethod
    def addOptionalSubElement(elem: Element, name: str, content: str = ""):
        """ ads+creates an optional element to an element (elem).
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
            newElem = TReqz.reqif_utils.createSubElement(name, content)
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
    def convertMd5ToReqifIdentifier(md5Hash: str):
        """ converts a md5-hash to a reqif identifier

        Arguments:
            md5Hash {str} -- the md5 hash (hex representation)

        Returns:
            {str} -- the reqif identifier
        """

        # example _63d2eb9d-0ed5-42ad-af40-7564803bdf4e
        return "_"+md5Hash[0:7]+"-"+md5Hash[8:11]+"-"+md5Hash[12:15]+"-"+md5Hash[16:19]+"-"+md5Hash[20:31]

    @staticmethod
    def generateNextLocalId(id_dict: TReqz.reqif_id_dict):
        """ this method generates a new local id (to store an element in id_dict)

        Arguments:
            id_dict {TReqz.reqif_id_dict} -- the current id_dict

        Returns:
            {str} -- the next id
        """

        currentId = id_dict.getLen()
        currentReqifIdentifier = None
        while currentReqifIdentifier == None or id_dict.get(currentReqifIdentifier) != None:
            currentId = currentId + 1
            currentHash = TReqz.reqif_utils.generateMd5(str(currentId))
            currentReqifIdentifier = TReqz.reqif_utils.convertMd5ToReqifIdentifier(
                currentHash)
        return currentReqifIdentifier
