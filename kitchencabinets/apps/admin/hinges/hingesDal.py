import models
from apps.admin.product.models import Product
from apps.admin.hinges.models import Hinges

def createHinges(hingesObj):
    
    """
    function is used to create the hinges
    """
    hingesDetails = models.Hinges(id=None,hinges_name=hingesObj.hinges_name,
                                       hinges_unit_price=hingesObj.hinges_unit_price,
                                       )
   
    hingesDetails.save()
    
    
    
def createProductHinges(hingesDict):
     
    """
    function is used to create the hinges
    """
    product = Product.objects.get(id=hingesDict['product_id'])
    hinges = Hinges.objects.get(id=hingesDict['hinges_id'])
    productHingesDetails = models.ProductHinges(id=None,product=product,hinges=hinges,hinges_min=hingesDict['minimum'],
                                       hinges_max=hingesDict['maximum']
                                       )
    productHingesDetails.save()
    
def listHinges():
    """
    Gets all details of all the hinges in the database
    
    :return HingesList: All the hinges
    """
    
    hingesList = models.Hinges.objects.all().order_by('id')
    return hingesList

def getHinges(hingesObj):
    """
    Gets all details of the given hinges 
    
    :param hingesObj:Holds the id of the string.Contains the following field,
                                                     id
    :type hingesObj: object                  
    :return hinges: return the hinges
    """
    hinges = models.Hinges.objects.get(pk=hingesObj.id)
    return hinges

def editHinges(hingesObj):
    """
    update the hinges information based on category id
    :param hingesObj: An object contains the following
                        id: Id of the hinges
    :type hingesObj: object 
    
   
    """
    
    hinges = models.Hinges.objects.get(pk=hingesObj.id) 
    hinges.hinges_name=hingesObj.hinges_name
    hinges.hinges_unit_price=hingesObj.hinges_unit_price
    hinges.save()
    
def deleteHinges(deleteObj):

    """
    delete the  hinges from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       hinges_id
                      
    
  
    """

    hinges = models.Hinges.objects.get(pk=deleteObj.id)
    hinges.delete()

def getProductHinges(productObj):
    """
    Gets hinges details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the hinges
    """
    hinges = models.ProductHinges.objects.filter(product=productObj.id)
    return hinges

def deleteProductHinges(hingesDict):
    
    """
        
        
    """
    productHinges = models.ProductHinges.objects.filter(product=hingesDict['product_id'])
    productHinges.delete()


def getExcludeProductHinges(productObj):
    productExcludeHInges = models.Hinges.objects.exclude(id__in=models.ProductHinges.objects.filter(product=productObj.id).values_list('hinges_id', flat=True))
    return productExcludeHInges
