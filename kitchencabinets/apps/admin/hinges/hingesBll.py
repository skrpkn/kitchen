import hingesDal


def createHinges(hingesObj):
     
    """
    function is used to create the hinges
    """
    hingesDal.createHinges(hingesObj)

def createProductHinges(hingesDict):
     
    """
    function is used to create the createProductHinges
    """
    hingesDal.createProductHinges(hingesDict)



def listHinges():
    """
    function is used to list all hinges
    """
    hingesList = hingesDal.listHinges()
    return hingesList

def getHinges(hingesObj):
    """
    Gets all details of the given hinges 
    
    :param hingesObj:Holds the id of the string.Contains the following field,
                                                     id
    :type hingesObj: object                  
    :return hinges: return the hinges
    """
    hinges = hingesDal.getHinges(hingesObj)
    return hinges

def editHinges(hingesObj):
    """
    update the hinges information based on sub category id
    :param hingesObj: An object contains the following
                        id: Id of the hinges
    :type hingesObj: object 
    
   
    """
    flag = hingesDal.editHinges(hingesObj)
    return flag

    
def deleteHinges(deleteObj):
    
    """
        
    """
    hingesDal.deleteHinges(deleteObj) 
    
def getProductHinges(productObj):
    """
    Gets hinges details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the hinges
    """
    hinges = hingesDal.getProductHinges(productObj)
    return hinges

def deleteProductHinges(hingesDict):
    
    """
        
    """
    hingesDal.deleteProductHinges(hingesDict)


# get all product cabinets    
def getExcludeProductHinges(productObj):  
   
    # get all product cabinets from mapping tables
    productHinges = hingesDal.getProductHinges(productObj)
    
    # get exclude lists
    productExcludeHinges = hingesDal.getExcludeProductHinges(productObj)  
    # append both 
    if len(productHinges) > 0:
        productExcludeHinges = list(productExcludeHinges)
        productExcludeHinges.extend(productHinges)
        
    return productExcludeHinges






