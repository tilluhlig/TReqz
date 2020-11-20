import os
import sys
sys.path.append(os.path.dirname(__file__)+"/../..")

import json
import requirements

def reqifToJson(reqifFile:str, documentPos:int = 0)->str:
    result = dict()
    reqif = requirements.TReqz.reqif(reqifFile)
    documentIds = reqif.getAllDocumentIds()
    
    documentId = documentIds[documentPos]
    typeId = reqif.getDocumentSpecObjectTypeId(documentId)
    
    # Attribute
    result["columns"] = reqif.getAllAttributeTypeLongNames(typeId)
    
    # Links
    linkData = list()
    links = reqif.getObjects(reqif.getLinkIds())
    
    for link in links:
        if link == None:
            continue
        
        sourceId = None if link.source == None else link.source.identifier
        targetId = None if link.target == None else link.target.identifier
        linkData.append({"source": sourceId, "target": targetId})
    result["links"] = linkData
    
    # Anforderungen
    allRequirements = reqif.getAllDocumentRequirementIds(documentId)
    reqData = list()
    for requirement in allRequirements:
        reqData.append({"id":requirement,
                        "content":reqif.getRequirementValues(requirement, convertEnums = True)})
    result["requirements"] = reqData
    
    return json.dumps(result)