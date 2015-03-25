import models
from apps.admin.product.models import Product
from apps.admin.cabinet.models import Cabinet
def createCabinet(cabinetObj):
    
    """
    function is used to create the cabinet
    """
    cabinetDetails = models.Cabinet(id=None,cabinet_name=cabinetObj.cabinet_name,
                                    width=cabinetObj.width,
                                    height=cabinetObj.height,
                                    depth=cabinetObj.depth
                                       )
   
    cabinetDetails.save()
    
def createProductCabinet(cabinetDict):
    
    """
    function is used to create the product cabinet
    """
    
    product = Product.objects.get(id=cabinetDict['product_id'])
    cabinet = Cabinet.objects.get(id=cabinetDict['cabinet_id'])
    productCabinetDetails = models.ProductCabinetConstruction(id=None,product=product,cabinet_construction=cabinet,
                                                              size=cabinetDict['size'],
                                       )
    productCabinetDetails.save()
    
def listCabinet():
    """
    Gets all details of all the cabinet in the database
    
    :return cabinetList: All the cabinet
    """
    
    cabinetList = models.Cabinet.objects.all().order_by('id')
    return cabinetList


def getCabinet(cabinetObj):
    """
    Gets all details of the given cabinet 
    
    :param cabinetObj:Holds the id of the string.Contains the following field,
                                                     id
    :type cabinetObj: object                  
    :return cabinet: return the cabinets
    """
    cabinets = models.Cabinet.objects.get(pk=cabinetObj.id)
    return cabinets

def editCabinet(cabinetObj):
    """
    update the cabinets information based on cabinet id
    :param cabinetObj: An object contains the following
                        id: Id of the hinges
    :type cabinetObj: object 
    
   
    """
    
    cabinets = models.Cabinet.objects.get(pk=cabinetObj.id) 
    cabinets.cabinet_name=cabinetObj.cabinet_name
    cabinets.width=cabinetObj.width
    cabinets.height=cabinetObj.height
    cabinets.depth=cabinetObj.depth
    cabinets.save()
    
        
def deleteCabinet(deleteObj):

    """
    delete the  cabinet from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       cabinet_id
                      
    
  
    """

    cabinets = models.Cabinet.objects.get(pk=deleteObj.id)
    cabinets.delete()
    
def getProductCabinet(productObj):
    """
    Gets product cabinet details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return product cabinet: return the product cabinet
    """
    productCabinet = models.ProductCabinetConstruction.objects.filter(product=productObj.id)
        
    return productCabinet


def getExcludeProductCabinet(productObj):
    
    productExcludeCabinet = models.Cabinet.objects.exclude(id__in=models.ProductCabinetConstruction.objects.filter(product=productObj.id).values_list('cabinet_construction_id', flat=True))
    return productExcludeCabinet

def deleteProductCabinet(cabinetDict):
    
    """
        
        
    """
    productCabinet = models.ProductCabinetConstruction.objects.filter(product=cabinetDict['product_id'])
    productCabinet.delete()


