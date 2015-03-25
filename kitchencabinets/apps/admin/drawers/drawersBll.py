import drawersDal


def createDrawers(drawersObj):
     
    """
    function is used to create the drawers
    """
    drawersDal.createDrawers(drawersObj)

def listDrawers():
    """
    function is used to list all drawers
    """
    drawersList = drawersDal.listDrawers()
    return drawersList

def getDrawers(drawersObj):
    """
    Gets all details of the given drawers 
    
    :param drawersObj:Holds the id of the string.Contains the following field,
                                                     id
    :type drawersObj: object                  
    :return drawers: return the drawers
    """
    drawers = drawersDal.getDrawers(drawersObj)
    return drawers

def editDrawers(drawersObj):
    """
    update the drawers information based on drawers id
    :param drawersObj: An object contains the following
                        id: Id of the drawers
    :type drawersObj: object 
    
   
    """
    flag = drawersDal.editDrawers(drawersObj)
    return flag


    
def deleteDrawers(deleteObj):
    
    """
        
    """
    drawersDal.deleteDrawers(deleteObj) 
    
    
def createProductDrawers(drawerDict):
     
    """
    function is used to create the createProduct drawer
    """
    drawersDal.createProductDrawers(drawerDict)
    
def getProductDrawers(productObj):
    """
    Gets product drawer details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the product drawers
    """
    drawers = drawersDal.getProductDrawers(productObj)
    return drawers

def deleteProductDrawer(drawerDict):
    
    """
        
    """
    drawersDal.deleteProductDrawer(drawerDict)

# get all product cabinets    
def getAllProductDrawers(productObj):  
    
    # get all product cabinets from mapping tables
    productDrawer = drawersDal.getProductDrawers(productObj)
    
    # get exclude lists
    productExcludeDrawer = drawersDal.getExcludeProductDrawers(productObj)  
    # append both 
    if len(productDrawer) > 0:
        productExcludeDrawer = list(productExcludeDrawer)
        productExcludeDrawer.extend(productDrawer)
        
    return productExcludeDrawer



