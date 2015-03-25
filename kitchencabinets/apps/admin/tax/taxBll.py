import taxDal

def createTaxes(taxObj):
    
    """
    function is used to create the tax
    """
    taxDal.createTaxes(taxObj)
    
    
def listAlActivelTax():
    """
    Gets all details of all the active taxes in the database
    
    :return CategoriesList: All the acive taxes
    """
    TaxList = taxDal.listAlActivelTax()
    return TaxList
def listAllTax():
    """
    Gets all details of all the taxes in the database
    
    :return CategoriesList: All the taxes
    """
    TaxList = taxDal.listAllTax()
    return TaxList


def editTax(taxObj):
    """
    update a tax information
    
    :param taxObj:Holds the id of the string.Contains the following field,
                                                    id
    :type taxObj: object                  
    """
    taxDal.editTax(taxObj)


def getTax(taxObj):
    """
    Gets all details of the given tax 
    
    :param taxObj:Holds the id of the string.Contains the following field,
                                                     id
    :type taxObj: object                  
    :return tax: return the tax
    """
    tax = taxDal.getTax(taxObj)
    return tax

def deleteTax(deleteObj):
    
    """
        
    """
    taxDal.deleteTax(deleteObj)

def taxMapping(taxDict):
    
    """
        
    """
    taxDal.taxMapping(taxDict)





def deleteProductTax(taxDict):
    
    """
        
    """
    taxDal.deleteProductTax(taxDict)

def getProductTaxes(productObj):
    """
    Gets product drawer details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the product drawers
    """
    taxes = taxDal.getProductTaxes(productObj)
    return taxes

# get all product cabinets    
def getAllProductTaxes(productObj):  
    
    # get all product cabinets from mapping tables
    productTax = taxDal.getProductTaxes(productObj)
    
    # get exclude lists
    productExcludeTaxes = taxDal.getExludedProductTaxes(productObj)
   
    # append both 
    if len(productTax) > 0:
        productExcludeTaxes = list(productExcludeTaxes)
        productExcludeTaxes.extend(productTax)
        
    return productExcludeTaxes



