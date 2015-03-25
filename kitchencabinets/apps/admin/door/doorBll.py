import doorDal


def createDoor(doorObj):
    
    """
    function is used to create the door
    """
    door_id = doorDal.createDoor(doorObj)
    
    return door_id
    
def createProductDoor(doorObj):
    
    """
    function is used to create a product door
    """
    doorDal.createProductDoor(doorObj)
    
    
def getExcludeProductDoors(productObj):  
   
    # get all product doors from mapping tables
    productDoors = doorDal.getProductDoor(productObj)
    # get exclude lists
    productExcludeDoors = doorDal.getExcludeProductDoors(productObj)
    # append both 
    if len(productDoors) > 0:
        productExcludeDoors = list(productExcludeDoors)
        productExcludeDoors.extend(productDoors)
    return productExcludeDoors

def listDoors():
    """
    Gets all details of all the doors in the database
    
    :return : All the Doors
    """
    DoorsList = doorDal.listDoors()
    return DoorsList

def deleteDoor(deleteObj):
    
    """
        
    """
    doorDal.deleteDoor(deleteObj)

def getDoor(doorObj):
    """
    Gets all details of the given door 
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    door = doorDal.getDoor(doorObj)
    return door

def getDoorColors(doorObj):
    """
    Gets door colors
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    door = doorDal.getDoorColors(doorObj)
    return door

def editDoor(editDoorObj):
    """
    update the category information based on category id
    :param editDoorObj: An object contains the following
                        id: Id of the category
    :type editDoorObj: object 
    
   
    """
    doorDal.editDoor(editDoorObj)
    
def getProductDoor(productObj):
    """
    Gets all details of the given door 
    
    :param doorObj:Holds the id of the string.Contains the following field,
                                                     id
    :type doorObj: object                  
    :return door: return the door
    """
    productDoor = doorDal.getProductDoor(productObj)
    return productDoor   

def editProductDoor(doorObj):
    
    """
    function is used to edit a product door
    """
    doorDal.editProductDoor(doorObj)


def deleteProductDoor(doorDict):
    
    """
    function is used to delete a product door
    """
    doorDal.deleteProductDoor(doorDict)

def createDoorColors(doorObj):
    
    """
    function is used to create the door colors
    """
    doorDal.createDoorColors(doorObj)



def listDoorColors():
    """
    Gets all details of all the door colors in the database
    
    :return : All the Door colors
    """
    DoorColorList = doorDal.listDoorColors()
    return DoorColorList

def deleteDoorColors(doorObj):
    
    """
    function is used to delete a  door colors
    """
    doorDal.deleteDoorColors(doorObj)



    