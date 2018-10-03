import shutil
import sys
import TReqz
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
import re
from lxml import etree
import io


class reqif_parser(TReqz.xml_parser):

    def __init__(self):
        pass

    def parseFile(self, contentFile: str):
        file = open(contentFile, "r")
        res = self.parse(file.read())
        file.close()
        return res

    def parse(self, content: str):
        root: Element = ET.fromstring(content)
        reqif: TReqz.reqif_req_if = TReqz.reqif_req_if(root)
        return reqif

    def dump(self, content: TReqz.reqif_req_if, pettyprint=True):
        xml: Element = content.encode()
        xmlData = ET.tostring(xml)
        #xmlResult = xmlData.decode("utf-8")
        root = etree.fromstring(xmlData)
        xmlData = etree.tostring(root, pretty_print=True, xml_declaration=True)
        xmlData = xmlData.decode("utf-8")
        return xmlData

    def dumpToFile(self, content: TReqz.reqif_req_if, fileName: str, pettyprint=True):
        file = open(fileName, "w")
        res = self.dump(content, pettyprint)
        file.write(res)
        file.close()
        return res
