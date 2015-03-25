import materialDal


def createMaterial(materialObj):
     
    """
    function is used to create the material
    """
    materialDal.createMaterial(materialObj)

def listMaterials(params= []):
    """
    Gets all details of all the Materials in the database
    
    :return materialsList: All the Materials
    """
    materialsList = materialDal.listMaterials(params)
    return materialsList

def getMaterial(materialObj):
    """
    Gets all details of the given Materials 
    
    :param cabinetObj:Holds the id of the string.Contains the following field,
                                                     id
    :type cabinetObj: object                  
    :return Materials: return the cabinets
    """
#     materials = materialDal.getMaterial(materialObj)
#     return materials


def editMaterial(materialObj):
    """
    update the cabinet information based on sub category id
    :param cabinetObj: An object contains the following
                        id: Id of the hinges
    :type cabinetObj: object 
    
   
    """
    flag = materialDal.editMaterial(materialObj)
    return flag

def deleteMaterial(deleteObj):
    
    """
    delete a material
    """
    materialDal.deleteMaterial(deleteObj) 