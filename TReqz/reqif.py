import TReqz
from .reqif_parser import reqif_parser
from .reqif_utils import reqif_utils
from xml.etree.ElementTree import Element
import re


class reqif:

    def __init__(self, filePath: str = None):
        __reqif_object: TReqz.reqif_req_if = None
        __id_dict = None

        if filePath != None:
            self.parseFile(filePath)

    def getHeader(self):
        """ returns the header object

        Returns:
            {reqif_req_if_header} -- the header object
        """

        return self.__reqif_object.req_if_header

    def parseFile(self, filePath: str):
        """ reads <filePath> and fills __reqif_object with the included reqif-content

        Arguments:
            filePath {str} -- a local reqif/reqifz file
        """

        self.__reqif_object: TReqz.reqif_req_if = reqif_parser.parseFile(
            filePath)
        self.__id_dict: TReqz.reqif_id_dict = self.__reqif_object.getIdDict()

    def dumpToFile(self, filePath: str, pettyprint=True):
        """ dumps the reqif object to <filePath>

        Arguments:
            filePath {str} -- a local file path (would be overwritten, if it exists)

        Keyword Arguments:
            pettyprint {bool} -- uses a pretty xml rendering mode (default: {True})
        """

        return reqif_parser.dumpToFile(
            self.__reqif_object, filePath, pettyprint)

    def addSpecObjectType(self, typeName: str, **kwargs):
        raise NotImplementedError

    def findSpecObjectTypeIdByLongName(self, longName: str):
        """ seeks to find a specObjectType-Id by its <longName> 

        Arguments:
            longName {str} -- the long-name

        Returns:
            [str/None] -- the id or None, if no object could be found
        """

        for specType in self.__reqif_object.req_if_content.spec_types:
            if specType.long_name == longName:
                return specType.identifier
        return None

    def findSpecObjectTypeByLongName(self, longName: str):
        """ seeks to find a specObjectType by its <longName>

        Arguments:
            longName {str} -- the long-name

        Returns:
            {str/None} -- the object or None, if no object could be found
        """

        id = self.findSpecObjectTypeIdByLongName(longName)
        return self.getObject(id)

    def findSpecObjectTypeIdByRequirementId(self, requirementId: str):
        """ seeks to find a specObjectType by a <requirementId>.
            the specObjectType is associated with the requirement.

        Arguments:
            requirementId {str} -- a requirement id

        Returns:
            {str/None} -- the id or None, if no object could be found
        """

        requirement = self.getObject(requirementId, TReqz.reqif_spec_object)
        return requirement.type.identifier

    def findSpecObjectTypeIdByAttributetTypeId(self, attributeId: str):
        """ seeks to find a specObjectType by a <attributeId>.
            the attribute is associated with the specObjectType.

        Arguments:
            attributeId {str} -- a attribute id

        Returns:
            {str/None} -- the id or None, if no object could be found
        """

        for specType in self.__reqif_object.req_if_content.spec_types:
            attributes = specType.spec_attributes
            for attribute in attributes:
                if attribute.identifier == attributeId:
                    return specType.identifier
        return None

    def getAllSpecObjectTypeLongNames(self):
        """ returns a list which contains the longNames of all existing specObjectTypes

        Returns:
            {list<str>} -- the long-names
        """

        longNames = list()
        for specType in self.__reqif_object.req_if_content.spec_types:
            longNames.append(specType.long_name)
        return longNames

    def getAllSpecObjectTypeIds(self):
        """ returns a list which contains the id's of all existing specObjectTypes

        Returns:
            {list<str>} -- the specObjectType id's
        """

        ids = list()
        for specType in self.__reqif_object.req_if_content.spec_types:
            ids.append(specType.identifier)
        return ids

    def addDatatype(self, typeName: str, **kwargs):
        raise NotImplementedError

    def findDatatypeIdByLongName(self, longName: str):
        """ seeks to find a dataType-id by its <longName>.

        Arguments:
            longName {str} -- the long-name

        Returns:
            {str/None} -- the id or None, if no object could be found
        """

        for datatype in self.__reqif_object.req_if_content.datatypes:
            if datatype.long_name == longName:
                return datatype.identifier
        return None

    def findDatatypeByLongName(self, longName: str):
        """ seeks to find a dataType by its <longName>.

        Arguments:
            longName {str} -- the long-name

        Returns:
            {str/None} -- the object or None, if no object could be found
        """

        id = self.findDatatypeIdByLongName(longName)
        return self.getObject(id)

    def getAllDatatypeLongNames(self):
        """ returns a list which contains the longNames of all existing dataTypes

        Returns:
            {list<str>} -- the long-names
        """

        longNames = list()
        for datatype in self.__reqif_object.req_if_content.datatypes:
            longNames.append(datatype.long_name)
        return longNames

    def getAllDatatypeIds(self):
        """returns a list which contains the id's of all existing dataTypes

        Returns:
            {list<str>} -- the id's
        """

        idList = list()
        for datatype in self.__reqif_object.req_if_content.datatypes:
            idList.append(datatype.identifier)
        return idList

    def getAttributeTypeValues(self, specObjectTypeId: str, attributetypeId: str):
        raise NotImplementedError  # for enums

    def addAttributeType(self, specObjectTypeId: str, longName: str, datatypeId: str, isEditable: str = "false"):
        raise NotImplementedError

    def findAttributeTypeIdByLongName(self, specObjectTypeId: str, longName: str):
        """ seeks to find a attributeType-id by its <longName> and the <specObjectTypeId>.

        Arguments:
            specObjectTypeId {str} -- a specObjectType-id
            longName {str} -- the long-name

        Returns:
            {str} -- the attribute-id
        """

        specType = self.getObject(specObjectTypeId)

        for attributeType in specType.spec_attributes:
            if attributeType.long_name == longName:
                return attributeType.identifier
        return None

    def findAttributeTypeByLongName(self, specObjectTypeId: str, longName: str):
        """ seeks to find a attributeType by its <longName> and the <specObjectTypeId>.

        Arguments:
            specObjectTypeId {str} -- a specObjectType-id
            longName {str} -- the long-name

        Returns:
            {reqif_attribute_definition} -- the attribute
        """

        id = self.findAttributeTypeIdByLongName(specObjectTypeId, longName)
        return self.getObject(id)

    def getAllAttributeTypeLongNames(self, specObjectTypeId: str):
        """ returns a list which contains the long-names of all existing attributes
            which are associated to a specObjectType <specObjectTypeId>

        Arguments:
            specObjectTypeId {str} -- the specObjectType-id

        Returns:
            {list<str>} -- the long-names
        """

        specType = self.getObject(specObjectTypeId)
        longNames = list()

        for attributeType in specType.spec_attributes:
            longNames.append(attributeType.longName)
        return longNames

    def checkAttributeIsEnumeration(self, attributeId: str):
        """ checks if an attribute is an enumeration

        Arguments:
            attributeId {str} -- the attribute id

        Returns:
            {bool} -- whether the attribute is an enumeration or not (true = yes, false = no)
        """

        attribute = self.getObject(attributeId)
        if "ENUMERATION" in attribute.name:
            return True
        return False

    def checkAttributeIsEnumerationByLongName(self, specObjectTypeId: str, attributeLongName: str):
        """ checks if an attribute is an enumeration

        Arguments:
            specObjectTypeId {str} -- a specObjectType-id which belongs to the attribute
            attributeLongName {str} -- the long-name of the attribute

        Returns:
            {bool} -- whether the attribute is an enumertion or not (true = yes, false = no)
        """

        attributeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        return self.checkAttributeIsEnumeration(attributeId)

    def convertEnumerationValues(self, attributeId: str, values: list):
        """ translates the key representations of the enumeration values by their long/real value

        Arguments:
            attributeId {str} -- the attribute-id
            values {list<str>} -- the values which should be translated

        Returns:
            {list<str>} -- the resolved values
        """

        attribute = self.getObject(attributeId)
        valueDefinitions = attribute.type.specified_values
        valueMap = dict()
        for possibleValues in valueDefinitions:
            valueMap[possibleValues.embedded_value.key] = possibleValues.long_name

        newValues = list()
        for value in values:
            newValues.append(valueMap[value])
        return newValues

    def convertEnumerationValuesByLongName(self, specObjectTypeId: str, attributeLongName: str, values: list):
        """ translates the key representations of the enumeration values by their long/real value

        Arguments:
            attributeLongName {str} -- the long-name of the attribute
            values {list<str>} -- the values which should be translated

        Returns:
            {list<str>} -- the resolved values
        """

        attributeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        return self.convertEnumerationValues(attributeId, values)

    def getAllAttributeTypeIds(self, specObjectTypeId: str):
        """ returns a list which contains the id's of all existing attributes
            which are included in a specObjectType <specObjectTypeId>

        Arguments:
            specObjectTypeId {str} -- a specObjectType-id

        Returns:
            {list<str>} -- the attribute id's
        """

        specType = self.getObject(specObjectTypeId)
        ids = list()

        for attributeType in specType.spec_attributes:
            ids.append(attributeType.identifier)
        return ids

    def __createSpecHierarchy(self, documentId: str, requirementId: str, parentSpecHierarchyId: str = None, is_table_internal: str = None, is_editable: str = None, last_change=None):
        """ creates a new specHierachy-object

        Arguments:
            documentId {str} -- the highe level document-id
            requirementId {str} -- the requirement which should be arranged in the hierarchy

        Keyword Arguments:
            parentSpecHierarchyId {str} -- [description] (default: {None})
            is_table_internal {str} -- [description] (default: {None})
            is_editable {str} -- True (yes) or False (no), depending on whether the attribute is editable or not 
            last_change {timestamp} -- [description] (default: {None})
        """

        if last_change == None:
            last_change = reqif_utils.current_timestamp()

        requirement = self.getObject(requirementId, TReqz.reqif_spec_object)
        document = self.getObject(documentId)
        parentSpecHierarchy = self.getObject(parentSpecHierarchyId)

        idDict = self.__reqif_object.getIdDict()
        newSpecHierarchy = reqif_utils.create_object_by_element_class(
            "reqif_spec_hierarchy", idDict)
        newSpecHierarchy.fill(
            req_object=requirement, is_table_internal=is_table_internal, is_editable=is_editable)

        if parentSpecHierarchyId == None:
            document.children.append(newSpecHierarchy)
        else:
            parentSpecHierarchy.children.append(newSpecHierarchy)

    def findSpecHierarchyByRequirementId(self, documentId: str, requirementId: str):
        """[summary]

        Arguments:
            documentId {str} -- [description]
            requirementId {str} -- [description]

        Returns:
            [type] -- [description]
        """

        specificationObject: TReqz.reqif_specification = self.getObject(
            documentId, TReqz.reqif_specification)

        children = list()+specificationObject.children
        i = 0
        while i < len(children):
            elem = children[i]
            if elem.req_object.identifier == requirementId:
                return elem.identifier
            children = children+elem.children
            i += 1
        return None

    def addRequirement(self, documentId: str, specObjectTypeId: str, parentRequirementId: str = None, last_change=None, long_name=None, alternative_id=None, desc=None, is_table_internal="false", is_editable="true"):
        """ adds a new requirement to the document <documentId>

        Arguments:
            documentId {str} -- the document-id where the requirement should be added
            specObjectTypeId {str} -- a specObjectType-id

        Keyword Arguments:
            parentRequirementId {str} -- an optional parent requirement to form a hierarchy (eg. Chapter/Folder) (default: {None})
            last_change {[type]} -- an optional timestamp. if None is given, the current time is used (default: {None})
            long_name {[type]} -- the requirement long-name/requirement id (default: {None})
            alternative_id {[type]} -- an optional alternative id (default: {None})
            desc {[type]} -- an optional description (default: {None})
            is_table_internal {str} -- whether the requirement is table internal (true = yes, false = no) (default: {"false"})
            is_editable {str} -- whether the requirement is editable (true = yes, false = no) (default: {"true"})

        Returns:
            {str} -- the new identifier or None if an error occured
        """

        if last_change == None:
            last_change = reqif_utils.current_timestamp()

        specObjects = self.__reqif_object.req_if_content.spec_objects
        specObjectType: TReqz.reqif_spec_object_type = self.getObject(
            specObjectTypeId, TReqz.reqif_spec_object_type)

        idDict = self.__reqif_object.getIdDict()
        newRequirement = reqif_utils.create_object_by_element_class(
            "reqif_spec_object", idDict)
        newRequirement.fill(type=specObjectType, last_change=last_change,
                            long_name=long_name, alternative_id=alternative_id, desc=desc)
        specObjects.append(newRequirement)

        parentSpecHierarchyId = None
        if parentRequirementId != None:
            parentSpecHierarchyId = self.findSpecHierarchyByRequirementId(
                documentId, parentRequirementId)
        self.__createSpecHierarchy(documentId, newRequirement.identifier, parentSpecHierarchyId,
                                   is_table_internal=is_table_internal, is_editable=is_editable, last_change=last_change)

        return newRequirement.identifier

    def findRequirementIdByLongName(self, longName: str):
        """ seeks to find a requirement-id by its <longName>.

        Arguments:
            longName {str} -- the long-name

        Returns:
            {str/None} -- the id or None, if no object could be found
        """

        for specObject in self.__reqif_object.req_if_content.spec_objects:
            if specObject.long_name == longName:
                return specObject.identifier
        return None

    def findRequirementIdsByFieldValue(self, field: str = None, value: str = None):
        """ seeks to find requirement-id's by a field-value combination.
            only the given/"not None" parameters (field, value) influencing the result.

        Keyword Arguments:
            field {str} -- an optional field-name. (default: {None})
            value {str} -- an optional value (default: {None})

        Returns:
            {list<str>} -- the requirement id's
        """

        requirementIds = list()
        for specObject in self.__reqif_object.req_if_content.spec_objects:
            for specObjectValue in specObject.values:
                fieldName = specObjectValue.definition.long_name
                if (fieldName != None and fieldName != field):
                    continue

                foundValue = False
                if value != None:
                    concreteValues = specObjectValue.getValue()
                    if isinstance(concreteValues, list):
                        for concreteValue in concreteValues:
                            if concreteValue == value:
                                foundValue = True
                                break
                    else:
                        if concreteValues == value:
                            break
                else:
                    foundValue = True

                if foundValue == True:
                    requirementIds.append(specObject.identifier)

        return requirementIds

    def findRequirementsByFieldValue(self, field: str = None, value: str = None):
        """ seeks to find requirements by a field-value combination.
            only the given/"not None" parameters (field, value) influencing the result.

        Keyword Arguments:
            field {str} -- an optional field-name. (default: {None})
            value {str} -- an optional value (default: {None})

        Returns:
            {list<reqif_spec_object>} -- the requirements
        """

        requirements = list()
        ids = self.findRequirementIdsByFieldValue(field, value)
        for id in ids:
            requirements.append(self.getObject(id))
        return requirements

    def addDocument(self, specificationTypeId: str):
        raise NotImplementedError

    def getAllDocumentIds(self):
        """ returns a list which contains all existing document-id's

        Returns:
            {list<str>} -- the id's
        """

        documentIds = list()
        for document in self.__reqif_object.req_if_content.specifications:
            documentIds.append(document.identifier)
        return documentIds

    def getAllDocuments(self):
        """ returns a list which contains all existing documents

        Returns:
            {list<reqif_specification>} -- the documents
        """

        documentIds = self.getAllDocumentIds()
        documents = list()
        for documentId in documentIds:
            documents.append(self.getObject(documentId))
        return documents

    def getAllDocumentRequirementIds(self, documentId):
        """ returns a list which contains all existing requirement-id's of a document <documentId>

        Returns:
            {list<str>} -- the requirement-id's
        """

        document = self.getObject(documentId)
        requirements = list()
        for specification in document.children:
            currentRequirements = list()
            currentSpecHierarchies = list()+specification.children
            i = 0
            while i < len(currentSpecHierarchies):
                specHierarchy: TReqz.reqif_spec_hierarchy = currentSpecHierarchies[i]
                currentRequirements.append(specHierarchy.req_object.identifier)
                currentSpecHierarchies = currentSpecHierarchies + specHierarchy.children
                i += 1
            requirements += currentRequirements
        return requirements

    def getAllRequirementIds(self):
        """ returns a list which contains all existing requirement-id's

        Returns:
            {list<str>} -- the requirement-id's
        """

        requirements = list()
        specifications = self.__reqif_object.req_if_content.specifications
        for specification in specifications:
            currentRequirements = list()
            currentSpecHierarchies = list()+specification.children
            i = 0
            while i < len(currentSpecHierarchies):
                specHierarchy: TReqz.reqif_spec_hierarchy = currentSpecHierarchies[i]
                currentRequirements.append(specHierarchy.req_object.identifier)
                currentSpecHierarchies = currentSpecHierarchies + specHierarchy.children
                i += 1
            requirements += currentRequirements
        return requirements

    def getHierarchicalRequirementIds(self):
        """ returns a list which contains the id's of all existing requirements (in hierarchical order)

        Returns:
            {dict<dict>} -- the requirement-id's
        """

        def collectIds(specHierarchy: TReqz.reqif_spec_hierarchy):
            requirements = dict()
            currentSpecHierarchies = specHierarchy.children
            for currentSpecHierarchie in currentSpecHierarchies:
                requirements[currentSpecHierarchie.req_object.identifier] = collectIds(
                    currentSpecHierarchie)
            return requirements

        requirements = dict()
        specifications = self.__reqif_object.req_if_content.specifications
        for specification in specifications:
            currentSpecHierarchies = list()+specification.children

            for currentSpecHierarchie in currentSpecHierarchies:
                requirements[currentSpecHierarchie.req_object.identifier] = collectIds(
                    currentSpecHierarchie)
        return requirements

    def __checkIfRequirementValueExists(self, requirementId: str, attributeId: str):
        """ check if the requireent value of <requirementId> exists, so it can be written

        Arguments:
            requirementId {str} -- the requirement-id
            attributeId {str} -- the corresponding attribute-id

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object

        Returns:
            {bool} -- whether the value-structure exists (true = yes, false = no)
        """

        element = self.getObject(requirementId, TReqz.reqif_spec_object)

        values = element.values
        for value in values:
            if value.definition.identifier == attributeId:
                return True
        return False

    def __createAttributeValue(self, requirementId: str, attributeId: str):
        """ creates a attribute-value reqif-structure element

        Arguments:
            requirementId {str} -- the id of the requirement where the new value should be added
            attributeId {str} -- the attribute type

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object
        """

        element = self.getObject(requirementId, TReqz.reqif_spec_object)
        attributeType = self.getObject(attributeId)

        valueClassName = TReqz.reqif_config.ATTRIBUTE_DEFINITION_TO_VALUE.get(
            type(attributeType).__name__)
        newAttributeValue = reqif_utils.create_object_by_element_class(
            valueClassName)
        newAttributeValue.fill(definition=attributeType)

        element.values.append(newAttributeValue)

    def setRequirementValues(self, requirementId: str, values: dict):
        """ sets a bulk of values for a requirement

        Arguments:
            requirementId {str} -- the requirement
            values {dict<str/list>} -- the values as field-value pairs
        """

        specObjectTypeId = self.findSpecObjectTypeIdByRequirementId(
            requirementId)

        for key in values:
            attributeLongName = key
            attributeId = self.findAttributeTypeIdByLongName(
                specObjectTypeId, attributeLongName)
            self.setRequirementValue(requirementId, attributeId, values[key])

    def setRequirementValue(self, requirementId: str, attributeId: str, value):
        """ sets a value for a requirement <requirementId>

        Arguments:
            requirementId {str} -- the requirement
            attributeId {str} -- the field/attribute
            value {str/list} -- the new value

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object
        """

        valueAlreadyExists: bool = self.__checkIfRequirementValueExists(
            requirementId, attributeId)

        if not valueAlreadyExists:
            self.__createAttributeValue(requirementId, attributeId)

        element = self.getObject(requirementId, TReqz.reqif_spec_object)

        values = element.values
        for elementValue in values:
            if elementValue.definition.identifier == attributeId:
                elementValue.setValue(value, self.__id_dict)
                break

    def setRequirementValueByAttributeLongName(self, requirementId: str, attributeLongName: str, value: list):
        """ sets a value for a requirement <requirementId>

        Arguments:
            requirementId {str} -- the requirement
            attributeLongName {str} -- the field/attribute (identified by its long-name)
            value {str/list} -- the new value

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object
        """

        specObjectTypeId = self.findSpecObjectTypeIdByRequirementId(
            requirementId)
        attributeTypeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        self.setRequirementValue(requirementId, attributeTypeId, value)

    def setRequirementValueByLongNames(self, requirementLongName: str, attributeLongName: str, value: list):
        """ sets a value for a requirement <requirementLongName>

        Arguments:
            requirementLongName {str} -- the requirement
            attributeLongName {str} -- the field/attribute (identified by its long-name)
            value {str/list} -- the new value
        """

        requirementId = self.findRequirementIdByLongName(requirementLongName)
        specObjectTypeId = self.findSpecObjectTypeIdByRequirementId(
            requirementId)
        attributeTypeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        self.setRequirementValue(requirementId, attributeTypeId, value)

    def getRequirementValue(self, requirementId: str, attributeTypeId: str, defaultValue: str = None):
        """ returns the value of a requirement field <attributeTypeId>

        Arguments:
            requirementId {str} -- the requirement
            attributeTypeId {str} -- the attribute/field

        Keyword Arguments:
            defaultValue {str} -- an optional default value if no field were found (default: {None})

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object

        Returns:
            {str/list} -- the value or the default value
        """

        element = self.getObject(requirementId, TReqz.reqif_spec_object)

        values = element.values
        for value in values:
            if value.definition.identifier == attributeTypeId:
                return value.getValue()
        return defaultValue

    def getRequirementValueByAttributeLongName(self, requirementId: str, attributeLongName: str, defaultValue: str = None):
        """ returns the value of a requirement field <attributeLongName>

        Arguments:
            requirementId {str} -- the requirement
            attributeLongName {str} -- the attribute/field identified by its long-name

        Keyword Arguments:
            defaultValue {str} -- an optional default value if no field were found (default: {None})

        Returns:
            {str/list} -- the value or the default value
        """

        specObjectTypeId = self.findSpecObjectTypeIdByRequirementId(
            requirementId)
        attributeTypeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        return self.getRequirementValue(requirementId, attributeTypeId, defaultValue)

    def getRequirementValueByLongNames(self, requirementLongName: str, attributeLongName: str, defaultValue: str = None):
        """ returns the value of a requirement field <attributeLongName>

        Arguments:
            requirementLongName {str} -- the long-name of a requirement
            attributeLongName {str} -- the attribute/field identified by its long-name

        Keyword Arguments:
            defaultValue {str} -- an optional default value if no field were found (default: {None})

        Returns:
            {str/list} -- the value or the default value
        """

        requirementId = self.findRequirementIdByLongName(requirementLongName)
        specObjectTypeId = self.findSpecObjectTypeIdByRequirementId(
            requirementId)
        attributeTypeId = self.findAttributeTypeIdByLongName(
            specObjectTypeId, attributeLongName)
        return self.getRequirementValue(requirementId, attributeTypeId, defaultValue)

    def getRequirementValues(self, requirementId: str):
        """ returns all existing fields+values for a requirement

        Arguments:
            requirementId {str} -- the requirement

        Raises:
            TypeError -- raises an error if the requirement-id doesn't belongs to an requirement-object

        Returns:
            {dict<str>} -- the values
        """

        element = self.getObject(
            requirementId, requiredType=TReqz.reqif_spec_object)

        reqValues = dict()
        values = element.values
        for value in values:
            reqValues[value.definition.long_name] = value.getValue()
        return reqValues

    def getRequirementValuesByLongName(self, requirementLongName: str):
        """ returns all existing fields+values for a requirement

        Arguments:
            requirementLongName {str} -- the requirement

        Returns:
            {dict<str>} -- the values
        """

        requirementId = self.findRequirementIdByLongName(requirementLongName)
        return self.getRequirementValues(requirementId)

    def getObject(self, objectId: str, requiredType=None):
        """ converts an object-id into an reqif object

        Arguments:
            objectId {str} -- the object-id

        Keyword Arguments:
            requiredType {__class__} -- an optional required result type (default: {None})

        Raises:
            TypeError -- raises an error if the objectId doesn't belongs to the requiredType

        Returns:
            {reqif_.../None} -- the object or None if no object were found
        """

        element = self.__reqif_object.reqif_dict.get(objectId)

        if requiredType != None and not isinstance(element, requiredType):
            raise TypeError("reqif_spec_object is required")

        return element

    def findUnreferencedObjects(self):
        """ finds reqif-elements which are not referenced by any other object

        Returns:
            {list<str>} -- a list of unreferenced objects
        """
        raise NotImplementedError

    def __checkIfObjectIsReferenced(self, objectId: str):
        """ checks if an object (objectId) is referenced by another object or not

        Arguments:
            objectId {str} -- the object-id

        Returns:
            {bool} -- true if the object is referenced by another object... false if not
        """
        return self.referenceMap.get(objectId) != None

    def __generateReferenceMap(self):
        """ generates a map which allows to check immediatly if an object is referenced by some

        Returns:
            {dict<bool>} -- shows if an object is referenced or not (true = yes, false = no)
        """

        self.referenceMap = dict()
        raise NotImplementedError

    def __checkIfStringIsWellFormedXml(content: str):
        """ checks if <content> is well formed xml

        Returns:
            {dict<bool>} -- true = is well formed, false = is not well formed
        """

        raise NotImplementedError
