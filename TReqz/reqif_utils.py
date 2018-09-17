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
        """ extracts the namespace from tag

        Arguments:
            tag {str} -- the tag

        Returns:
            {str} -- the namespace
        """

        namespace = re.match("\{.*\}", tag)
        return namespace.group(0) if namespace else ''

    @staticmethod
    def generate_local_ref_list_from_elements(content: Element, id_dict: TReqz.reqif_id_dict, elements_parent_path: str):
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            elements_parent_path {str} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            elements_parent_path {str} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            element_path {str} -- [description]

        Returns:
            [type] -- [description]
        """

        elem: Element = content.find(element_path)
        id = id_dict.get(elem.get("IDENTIFIER"))

        if id == None:
            print("missing local ref: "+elem.get("IDENTIFIER"))
            return None

        return id

    @staticmethod
    def get_text_from_element(content: Element, element_path: str):
        """[summary]

        Arguments:
            content {Element} -- [description]
            element_path {str} -- [description]

        Returns:
            [type] -- [description]
        """

        elem: Element = content.find(element_path)
        if elem == None:
            return None
        return elem.text

    @staticmethod
    def get_element(content: Element, element_path: str):
        """[summary]

        Arguments:
            content {Element} -- [description]
            element_path {str} -- [description]

        Returns:
            [type] -- [description]
        """

        elem: Element = content.find(element_path)
        return elem

    @staticmethod
    def get_local_ref_from_element_text(content: Element, id_dict: TReqz.reqif_id_dict, element_path: str):
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            element_path {str} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            elements_parent_path {str} -- [description]
            typeList {dict} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Returns:
            [type] -- [description]
        """
        return datetime.datetime.now(pytz.utc).isoformat()

    @staticmethod
    def create_object_by_element_class(type: str, id_dict: TReqz.reqif_id_dict = None):
        """[summary]

        Arguments:
            id_dict {TReqz.reqif_id_dict} -- [description]
            type {str} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            content {Element} -- [description]
            id_dict {TReqz.reqif_id_dict} -- [description]
            element_path {str} -- [description]
            type {str} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            target {Element} -- [description]
            source {Element} -- [description]
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
        """[summary]

        Arguments:
            elem {Element} -- [description]
            attribute {str} -- [description]
            value {str} -- [description]
        """

        if value != None:
            elem.set(attribute, value)

    @staticmethod
    def createSubElement(name: str, content: str = None):
        """[summary]

        Arguments:
            name {str} -- [description]

        Keyword Arguments:
            content {str} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """

        newElem = Element(name)
        if content != None:
            newElem.text = content
        return newElem

    @staticmethod
    def addRequiredSubElement(elem: Element, name: str, content: str = None):
        """[summary]

        Arguments:
            elem {Element} -- [description]
            name {str} -- [description]

        Keyword Arguments:
            content {str} -- [description] (default: {None})

        Returns:
            [type] -- [description]
        """

        newElem = TReqz.reqif_utils.createSubElement(name, content)
        elem.append(newElem)
        return newElem

    @staticmethod
    def addOptionalSubElement(elem: Element, name: str, content: str = ""):
        """[summary]

        Arguments:
            elem {Element} -- [description]
            name {str} -- [description]

        Keyword Arguments:
            content {str} -- [description] (default: {""})

        Returns:
            [type] -- [description]
        """

        if content != None:
            newElem = TReqz.reqif_utils.createSubElement(name, content)
            elem.append(newElem)
            return newElem
        return None

    @staticmethod
    def addEncodedSubElement(elem: Element, subElem):
        """[summary]

        Arguments:
            elem {Element} -- [description]
            subElem {[type]} -- [description]

        Returns:
            [type] -- [description]
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
        """[summary]

        Arguments:
            md5Hash {str} -- [description]

        Returns:
            [type] -- [description]
        """

        # example _63d2eb9d-0ed5-42ad-af40-7564803bdf4e
        return "_"+md5Hash[0:7]+"-"+md5Hash[8:11]+"-"+md5Hash[12:15]+"-"+md5Hash[16:19]+"-"+md5Hash[20:31]

    @staticmethod
    def generateNextLocalId(id_dict: TReqz.reqif_id_dict):
        """[summary]

        Arguments:
            id_dict {TReqz.reqif_id_dict} -- [description]

        Returns:
            [type] -- [description]
        """

        currentId = id_dict.getLen()
        currentReqifIdentifier = None
        while currentReqifIdentifier == None or id_dict.get(currentReqifIdentifier) != None:
            currentId = currentId + 1
            currentHash = TReqz.reqif_utils.generateMd5(str(currentId))
            currentReqifIdentifier = TReqz.reqif_utils.convertMd5ToReqifIdentifier(
                currentHash)
        return currentReqifIdentifier
