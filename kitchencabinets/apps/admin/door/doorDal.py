import models
from apps.admin.product.models import Product

def createDoor(doorObj):
    
    """
    function is used to create the door
    """
    doorDetails = models.Doors(door_id=None,door_name=doorObj.door_name,
                                       door_price=doorObj.door_price,
                                       estimated_time=doorObj.estimated_time,
                                       description=doorObj.description
                                       )
    doorDetails.save()
    return doorDetails.pk

def createProductDoor(doorDict):
    
    """
    function is used to create the product door
    """
    product = Product.objects.get(id=doorDict['product_id'])
    door = models.Doors.objects.get(door_id=doorDict['door_id'])
    productDoorDeatails = models.ProductDoors(id=None,product=product,
                                       door=door,
                                       pieces_count=doorDict['door_piece']
                                       )
    productDoorDeatails.save()

def listDoors():
    """
    Gets all details of all the doors in the database
    
    :return DoorsList: All the doors
    """
        
    DoorsList = models.Doors.objects.all()
    return DoorsList


    
def deleteDoor(deleteObj):

    """
    delete the  door from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       doorId
                      
    
  
    """
    deleteDoorColors(deleteObj)
    Door = models.Doors.objects.get(pk=deleteObj.id)
    Door.delete()
    
    
def getDoor(doorObj):
    """
    Gets all details of the given door 
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    door = models.Doors.objects.get(pk=doorObj.id)
    return door



def editDoor(editDoorObj):
    """
    update the category information based on category id
    :param editDoorObj: An object contains the following
                        id: Id of the category
    :type editDoorObj: object 
    
   
    """
    
    door = models.Doors.objects.get(pk=editDoorObj.id) 
    door.door_name=editDoorObj.door_name
    door.door_price=editDoorObj.door_price
    door.estimated_time=editDoorObj.estimated_time
    door.description=editDoorObj.description
    door.save()

def getProductDoor(productObj):
    """
    Gets all details of the given door 
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    productDoor = models.ProductDoors.objects.filter(product=productObj.id)
    return productDoor 


def editProductDoor(doorObj):
    
    """
    function is used to edit a product door
    """
    productDoor = models.ProductDoors.objects.get(product=doorObj.product_id)
    door = models.Doors.objects.get(door_id=doorObj.door_id)
    productDoor.door = door
    productDoor.save()



def deleteProductDoor(doorDict):
    
    """
    function is used to delete a product door
    """
    
    productDoor = models.ProductDoors.objects.filter(product=doorDict['product_id'])
    productDoor.delete()

def createDoorColors(doorObj):
    """
    function is used to create the door colors
    """
    Door = models.Doors.objects.get(door_id=doorObj.door_id)
    doorColors = models.DoorColors(id=None,door=Door,
                                       color_code=doorObj.color
                                       )
    doorColors.save()


def listDoorColors():
    """
    Gets all details of all the door colors in the database
    
    :return : All the Door colors
    """
    
    DoorColorList = models.DoorColors.objects.all()
    return DoorColorList

def getDoorColors(doorObj):
    """
    Gets door colors
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    
    door = models.DoorColors.objects.filter(door=doorObj.id)
    return door

def deleteDoorColors(doorObj):
    
    """
    function is used to delete a  door colors
    """
    doorColors = models.DoorColors.objects.filter(door=doorObj.id)
    doorColors.delete()


def getExcludeProductDoors(productObj):
    productExcludeDoors = models.Doors.objects.exclude(door_id__in=models.ProductDoors.objects.filter(product=productObj.id).values_list('door_id', flat=True))
    return productExcludeDoors
