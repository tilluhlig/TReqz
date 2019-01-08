import xml.etree.cElementTree as ET
from libs.Requirements import TReqz as TReqz
from xml.etree.ElementTree import Element as Element
import unittest

class utils:
    
    @staticmethod
    def getIdentifiableAttributes()->dict:
        return {"DESC":"desc", "IDENTIFIER":"identifier", "LAST-CHANGE":"last_change", "LONG-NAME":"long_name"}
    
    @staticmethod
    def decodeObj(obj, xmlContent:str, id_dict=None):
        elem:Element = ET.fromstring(xmlContent)
        obj.decode(elem, id_dict)
        
    @staticmethod
    def testDecodeLocalRefFromElementText(self, obj, xmlContent:str, reqifAttributeName:str, testIdentifier:str):
        id_dict = TReqz.reqif_id_dict()
        utils.decodeObj(obj, "<"+obj.name+">"+xmlContent+"</"+obj.name+">", id_dict)
        self.assertEqual(None, obj.get(reqifAttributeName))

        newIdentifiable = TReqz.reqif_identifiable()
        newIdentifiable.identifier=testIdentifier
        id_dict.add(newIdentifiable)
        utils.decodeObj(obj, "<"+obj.name+">"+xmlContent+"</"+obj.name+">", id_dict)
        self.assertEqual(testIdentifier, obj.get(reqifAttributeName).identifier)
        obj.fill(**{reqifAttributeName:None})

    @staticmethod
    def testDecodeAttribute(self, obj, reqifAttributeName:str, attributeName:str, attributeValue:str='A'):
        utils.decodeObj(obj, "<"+obj.name+" "+attributeName+"='"+attributeValue+"' />")
        self.assertEqual(attributeValue, obj.get(reqifAttributeName))
        obj.fill(**{reqifAttributeName:None})

    @staticmethod
    def testDecodeIdentifiableAttributes(self, obj):
        for xmlAttributeName, reqifAttributeName in utils.getIdentifiableAttributes().items():
            utils.testDecodeAttribute(self, obj, reqifAttributeName, xmlAttributeName, xmlAttributeName+"1")
            obj.fill(**{reqifAttributeName:None})

    @staticmethod
    def encodeObj(obj, fillContent:dict)->str:
        obj.fill(**fillContent)
        encodedObj = obj.encode()
        xmlContent = ET.tostring(encodedObj, encoding='utf-8', method='xml')
        xmlContent:str = xmlContent.decode("utf-8")
        return xmlContent
        
    @staticmethod
    def testEncodeLocalRefFromElementText(self, obj, xmlTestReference:str, reqifAttributeName:str, testIdentifier:str):
        newIdentifiable = TReqz.reqif_identifiable()
        newIdentifiable.identifier=testIdentifier
        xmlContent = utils.encodeObj(obj,{reqifAttributeName:newIdentifiable})
        self.assertEqual("<"+obj.name+">"+xmlTestReference+"</"+obj.name+">", xmlContent)
        obj.fill(**{reqifAttributeName:None})
        
    @staticmethod
    def testEncodeAttribute(self, obj, reqifAttributeName:str, xmlAttributeName:str, attributeValue:str='A'):
        xmlContent = utils.encodeObj(obj,{reqifAttributeName:attributeValue})
        self.assertEqual("<"+obj.name+" "+xmlAttributeName+"=\""+attributeValue+"\" />", xmlContent)
        obj.fill(**{reqifAttributeName:None})

    @staticmethod
    def testEncodeIdentifiableAttributes(self, obj):
        for xmlAttributeName, reqifAttributeName in utils.getIdentifiableAttributes().items():
            utils.testEncodeAttribute(self, obj, reqifAttributeName, xmlAttributeName, xmlAttributeName+"1")