import TReqz
from  xml.etree.ElementTree import Element
import re

class utils:
    @staticmethod
    def createDatatype(reqifObject:TReqz.reqif_req_if, typeName:str, **kwargs):
       print("not implemented!!!")

    @staticmethod
    def findDatatypeIdByLongName(reqifObject:TReqz.reqif_req_if, name:str):
       for datatype in reqifObject.req_if_content.datatypes:
           if datatype.long_name == name:
               return datatype.identifier
       return None

    @staticmethod
    def findDatatypeByLongName(reqifObject:TReqz.reqif_req_if, name:str):
       id = TReqz.utils.findDatatypeIdByLongName(reqifObject, name)
       return TReqz.utils.getObject(reqifObject, id)

    @staticmethod
    def getAllDatatypeLongNames(reqifObject:TReqz.reqif_req_if):
        longNames = list()
        for datatype in reqifObject.req_if_content.datatypes:
            longNames.append(datatype.long_name)
        return longNames

    @staticmethod
    def getAllDatatypeIds(reqifObject:TReqz.reqif_req_if):
        idList = list()
        for datatype in reqifObject.req_if_content.datatypes:
            idList.append(datatype.identifier)
        return idList

    @staticmethod
    def createAttributeType(reqifObject:TReqz.reqif_req_if, datatypeId:str):
       print("not implemented!!!")

    @staticmethod
    def findAttributeTypeByLongName(reqifObject:TReqz.reqif_req_if, name:str):
       print("not implemented!!!")

    @staticmethod
    def getAllAttributeTypeLongNames(reqifObject:TReqz.reqif_req_if):
       print("not implemented!!!")

    @staticmethod
    def getAllAttributeTypes(reqifObject:TReqz.reqif_req_if):
       print("not implemented!!!")

    @staticmethod
    def createRequirement(reqifObject:TReqz.reqif_req_if, attributeTypeId:str):
       print("not implemented!!!")

    @staticmethod
    def findRequirementIdByLongName(reqifObject:TReqz.reqif_req_if, name:str):
       for specObject in reqifObject.req_if_content.spec_objects:
           if specObject.long_name == name:
               return specObject.identifier
       return None

    @staticmethod
    def findRequirementIdsByFieldValue(reqifObject:TReqz.reqif_req_if, field:str=None, value:str=None):
       requirementIds = list()
       for specObject in reqifObject.req_if_content.spec_objects:
           for specObjectValue in specObject.values:
               fieldName = specObjectValue.definition.long_name
               if (fieldName != None and fieldName != field):
                   continue

               foundValue = False
               if value != None:
                    concreteValues = specObjectValue.getValues()
                    for concreteValue in concreteValues:
                        if concreteValue == value:
                            foundValue=True
                            break
               else:
                    foundValue = True

               if foundValue == True:
                    requirementIds.append(specObject.identifier)

       return requirementIds

    @staticmethod
    def findRequirementsByFieldValue(reqifObject:TReqz.reqif_req_if, field:str=None, value:str=None):
       requirements = list()
       ids = TReqz.utils.findRequirementIdsByFieldValue(reqifObject, field, value)
       for id in ids:
           requirements.append(TReqz.utils.getObject(reqifObject, id))
       return requirements

    @staticmethod
    def addDocument(reqifObject:TReqz.reqif_req_if):
       print("not implemented!!!")

    @staticmethod
    def getAllRequirementIds(reqifObject:TReqz.reqif_req_if):
       requirements = list()
       specifications = reqifObject.req_if_content.specifications 
       for specification in specifications:
           currentRequirements = list()
           currentSpecHierarchies = list()+specification.children
           i = 0
           while i<len(currentSpecHierarchies):
             specHierarchy:TReqz.reqif_spec_hierarchy = currentSpecHierarchies[i]
             currentRequirements.append(specHierarchy.req_object.identifier)
             currentSpecHierarchies = currentSpecHierarchies + specHierarchy.children
             i+=1
           requirements.append(currentRequirements)
       return requirements   

    @staticmethod
    def getObject(reqifObject:TReqz.reqif_req_if, id:str):
        return reqifObject.reqif_dict.get(id)