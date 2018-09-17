import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import ElementTree
import re
import TReqz


class reqif_id_dict(object):

    def __init__(self):
        self.identifiers = dict()  # reqif_identifiable

    def getLen(self):
        return len(self.identifiers)

    def add(self, newElem: TReqz.reqif_identifiable):
        self.identifiers[newElem.identifier] = newElem

    def get(self, name: str):
        return self.identifiers.get(name)

    def getIdentifierByObject(self, elem: TReqz.reqif_identifiable):
        return elem.identifier

    def remove(self, name: str):
        return self.identifiers.pop(name)
