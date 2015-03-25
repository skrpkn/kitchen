import models


def createTaxes(taxObj):
    
    """
    function is used to create the tax
    """
    taxDetails = models.Tax(id=None,tax_name=taxObj.tax_name,
                                       tax_date=taxObj.tax_date,
                                       tax_status=taxObj.tax_status,
                                       tax_rate=taxObj.tax_rate
                                       )
    taxDetails.save()
    


def listAllTax():
    """
    Gets all details of all the taxes in the database
    
    :return CategoriesList: All the taxes
    """
    TaxList = models.Tax.objects.all().order_by('tax_name')
    return TaxList

def listAlActivelTax():
    """
    Gets all details of all the taxes in the database
    
    :return CategoriesList: All the taxes
    """
    TaxList = models.Tax.objects.filter(tax_status='active')
    return TaxList


def getTax(taxObj):
    """
    Gets all details of the given tax 
    
    :param taxObj:Holds the id of the string.Contains the following field,
                                                     id
    :type taxObj: object                  
    :return tax: return the tax
    """
    tax = models.Tax.objects.get(pk=taxObj.id)
    return tax

def editTax(taxObj):
    """
    update a tax information
    
    :param taxObj:Holds the id of the string.Contains the following field,
                                                    id
    :type taxObj: object                  
    """
    tax = models.Tax.objects.get(pk=taxObj.id)
    tax.tax_name=taxObj.tax_name
    tax.tax_status=taxObj.tax_status
    tax.tax_date=taxObj.tax_date
    tax.tax_rate=taxObj.tax_rate
    tax.save()

def deleteTax(deleteObj):
    
    """
        
    """
    tax = models.Tax.objects.get(pk=deleteObj.id)
    tax.delete()
   

def taxMapping(taxDict):
    """
        
    """
    product = models.Product.objects.get(id=taxDict['product_id'])
    tax = models.Tax.objects.get(id=taxDict['tax_id'])
    
    productTaxDetails = models.TaxMapping(id=None,product=product,
                                tax=tax
                               )
    
    productTaxDetails.save()
   
    
def deleteProductTax(taxDict):
    
    """
        
        
    """
    productTaxDetails = models.TaxMapping.objects.filter(product=taxDict['product_id'])
    productTaxDetails.delete()    
    

def getProductTaxes(productObj):
    """
    Gets product drawer details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the product drawers
    """
    
    taxes = models.TaxMapping.objects.filter(product=productObj.id)
    return taxes


def getExludedProductTaxes(productObj):
    productExcludeTaxes = models.Tax.objects.exclude(id__in=models.TaxMapping.objects.filter(product=productObj.id).values_list('tax_id', flat=True)).filter(tax_status='active')
    return productExcludeTaxes