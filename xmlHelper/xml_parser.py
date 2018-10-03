
class xml_parser(object):
    """ this class represents a parser interface
    """

    def __init__(self):
        pass

    def parseFile(self, contentFile: str)->None:
        raise NotImplementedError

    def parse(self, content: str)->None:
        raise NotImplementedError

    def dump(self, content, pettyprint=True)->None:
        raise NotImplementedError

    def dumpToFile(self, content, fileName: str, pettyprint=True)->None:
        raise NotImplementedError
