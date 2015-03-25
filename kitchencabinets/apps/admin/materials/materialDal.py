import models
from apps.admin.product.models import Product
from apps.admin.product import productBll

def createMaterial(materialObj):
    
    """
    function is used to create the materails
    """
    materialDetails = models.Materials(id=None,name=materialObj.name,
                                       price=materialObj.price,
                                       description=materialObj.description,
                                       status=materialObj.status
                                       )
   
    materialDetails.save()
    
def listMaterials(params):
    """
    Gets all details of all the Materials in the database
    
    :return materialsList: All the Materials
    """
          
    materialsList = models.Materials.objects
    if 'status' in params:
        materialsList = materialsList.filter(status=params['status'])
    
    if 'id' in params:
        materialsList = materialsList.get(pk=params['id'])
        
    if len(params) == 0:
        materialsList = materialsList.all().order_by('id')  
    
    
    return materialsList

def editMaterial(materialObj):
    """
    update the cabinets information based on cabinet id
    :param cabinetObj: An object contains the following
                        id: Id of the hinges
    :type cabinetObj: object 
    
   
    """
    
    materials = models.Materials.objects.get(pk=materialObj.id) 
    materials.name=materialObj.name
    materials.price=materialObj.price
    materials.description=materialObj.description
    materials.status=materialObj.status
    materials.save()
    
    
def deleteMaterial(deleteObj):

    """
    delete the  material from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       materialId
    """
    productList = Product.objects.filter(material=deleteObj.id)
    if(productList):
        for product in productList:
            try:
                productBll.deleteProducts(product)
            except:
                pass
    material = models.Materials.objects.get(pk=deleteObj.id)
    try:
        material.delete()
    except:
                pass
    
    