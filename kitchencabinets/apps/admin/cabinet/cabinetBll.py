import cabinetDal


def createCabinet(cabinetObj):
     
    """
    function is used to create the cabinet
    """
    cabinetDal.createCabinet(cabinetObj)
    
def checkFormula(cabinetObj):
    """
    check formula 
    """
    if 'width' in cabinetObj.formulaList:
        cabinetObj.width=1
    else:
        cabinetObj.width=2
    if 'height' in cabinetObj.formulaList:
        cabinetObj.height=1
    else:
        cabinetObj.height=2
    if 'depth' in cabinetObj.formulaList:
        cabinetObj.depth=1
    else:
        cabinetObj.depth=2
    return cabinetObj
    
def createProductCabinet(cabinetDict):
     
    """
    function is used to create the product cabinet
    """
    cabinetDal.createProductCabinet(cabinetDict)

def listCabinet():
    """
    function is used to list all cabinet
    """
    cabinetList = cabinetDal.listCabinet()
    return cabinetList

def getCabinet(cabinetObj):
    """
    Gets all details of the given cabinet 
    
    :param cabinetObj:Holds the id of the string.Contains the following field,
                                                     id
    :type cabinetObj: object                  
    :return cabinets: return the cabinets
    """
    cabinets = cabinetDal.getCabinet(cabinetObj)
    return cabinets

def editCabinet(cabinetObj):
    """
    update the cabinet information based on sub category id
    :param cabinetObj: An object contains the following
                        id: Id of the hinges
    :type cabinetObj: object 
    
   
    """
    flag = cabinetDal.editCabinet(cabinetObj)
    return flag

    
def deleteCabinet(deleteObj):
    
    """
        
    """
    cabinetDal.deleteCabinet(deleteObj) 
    
    
def getProductCabinet(productObj):
    """
    Gets product cabinet details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return product cabinet: return the product cabinet
    """
    productCabinet = cabinetDal.getProductCabinet(productObj)
    return productCabinet

def deleteProductCabinet(cabinetDict):
    
    """
        
    """
    cabinetDal.deleteProductCabinet(cabinetDict) 
    
def getExcludeProductCabinet(productObj):   
    productExcludeCabinet = cabinetDal.getExcludeProductCabinet(productObj)  
    return productExcludeCabinet
    
# get all product cabinets    
def getAllProductCabinet(productObj):   
    
    
    # get all product cabinets from mapping tables
    productCabinet = cabinetDal.getProductCabinet(productObj)
    # get exclude lists
    productExcludeCabinet = cabinetDal.getExcludeProductCabinet(productObj)  
    # append both 
    if len(productCabinet) > 0:
        productExcludeCabinet = list(productExcludeCabinet)
        productExcludeCabinet.extend(productCabinet)
    return productExcludeCabinet
    
    
    
    
    
    
    
    
    
    
    
    
