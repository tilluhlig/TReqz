#import os
import shutil
#import json
import sys
import TReqz
import xml.etree.cElementTree as ET
from  xml.etree.ElementTree import Element
from  xml.etree.ElementTree import ElementTree
import re
from lxml import etree
import io

class reqif_parser(object):
    
   @staticmethod
   def parseFile(contentFile:str):
        file = open(contentFile, "r")
        res = reqif_parser.parse(file.read())
        file.close()
        return res
    
   @staticmethod
   def parse(content:str):
        root:Element = ET.fromstring(content)
        reqif:TReqz.reqif_req_if = TReqz.reqif_req_if(root)
        return reqif

   @staticmethod
   def dump(content:TReqz.reqif_req_if, pettyprint=True):
     xml:Element = content.encode()
     xmlData = ET.tostring(xml)
     #xmlResult = xmlData.decode("utf-8")
     root = etree.fromstring(xmlData)
     xmlData = etree.tostring(root, pretty_print=True, xml_declaration=True)
     xmlData = xmlData.decode("utf-8")
     return xmlData

   @staticmethod
   def dumpToFile(content:TReqz.reqif_req_if, fileName:str, pettyprint=True):
        file = open(fileName, "w")
        res = reqif_parser.dump(content, pettyprint)
        file.write(res)
        file.close()
        return res
     