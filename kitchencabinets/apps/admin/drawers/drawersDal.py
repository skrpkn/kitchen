import models
from apps.admin.product.models import Product

def createDrawers(drawersObj):
    
    """
    function is used to create the drawers
    """
    drawersDetails = models.Drawers(id=None,drawer_name=drawersObj.drawer_name,
                                       drawer_unit_price=drawersObj.drawer_unit_price,
                                       )
   
    drawersDetails.save()

    
def listDrawers():
    """
    Gets all details of all the drawers in the database
    
    :return drawersList: All the drawers
    """
    
    drawersList = models.Drawers.objects.all().order_by('id')
    return drawersList

def getDrawers(drawersObj):
    """
    Gets all details of the given drawers 
    
    :param drawersObj:Holds the id of the string.Contains the following field,
                                                     id
    :type drawersObj: object                  
    :return drawers: return the drawers
    """
    drawers = models.Drawers.objects.get(pk=drawersObj.id)
    return drawers


def editDrawers(drawersObj):
    """
    update the drawers information based on drawers id
    :param drawersObj: An object contains the following
                        id: Id of the drawers
    :type drawersObj: object 
    
   
    """
    
    drawers = models.Drawers.objects.get(pk=drawersObj.id) 
    drawers.drawer_name=drawersObj.drawer_name
    drawers.drawer_unit_price=drawersObj.drawer_unit_price
    drawers.save()
    
       
def deleteDrawers(deleteObj):

    """
    delete the  drawers from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       drawers_id
                      
    
  
    """

    hinges = models.Drawers.objects.get(pk=deleteObj.id)
    hinges.delete()
        
def createProductDrawers(drawerDict):
     
    """
    function is used to create the createProduct drawer
    """
    product = Product.objects.get(id=drawerDict['product_id'])
    drawer = models.Drawers.objects.get(id=drawerDict['drawer_id'])
    productDrawerDetails = models.ProductDrawers(id=None,product=product,drawer=drawer, 
                                product_drawers_quantity=drawerDict['drawer_qty'],
                                product_drawer_total_price=drawerDict['drawer_total_price']
                                       )
    productDrawerDetails.save()
    
    
    
def getProductDrawers(productObj):
    """
    Gets product drawer details
    
    :param productObj:Holds the id of the string.Contains the following field,
                                                     id
    :type productObj: object                  
    :return hinges: return the product drawers
    """
    
    drawers = models.ProductDrawers.objects.filter(product=productObj.id)
    return drawers

def deleteProductDrawer(drawerDict):
    
    """
        
        
    """
    productDrawerDetails = models.ProductDrawers.objects.filter(product=drawerDict['product_id'])
    productDrawerDetails.delete()



def getExcludeProductDrawers(productObj):
    productExcludeDrawers = models.Drawers.objects.exclude(id__in=models.ProductDrawers.objects.filter(product=productObj.id).values_list('drawer_id', flat=True))
    return productExcludeDrawers

