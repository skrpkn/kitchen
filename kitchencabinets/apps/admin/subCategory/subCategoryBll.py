import subCategoryDal




def filterSubCategories(subCategoryObj):
    """
    Gets all details of filtered in the database
    
    :return SubCategoriesList: All the SubCategories
    """
    FilteredSubCategoriesList = subCategoryDal.filterSubCategories(subCategoryObj)
    return FilteredSubCategoriesList

def getAllSubCategories():
    """
    Gets all details of all the SubCategories in the database
    
    :return SubCategoriesList: All the SubCategories
    """
    SubCategoriesList = subCategoryDal.getAllSubCategories()
    return SubCategoriesList

def createSubCategory(subCategoryObj):
    
    """
    function is used to create the sub category
    """
    flag = subCategoryDal.createSubCategory(subCategoryObj)
    return flag

def deleteSubCategory(deleteObj):
    
    """
        
    """
    subCategoryDal.deleteSubCategory(deleteObj)

def getSubCategory(subCategoryObj):
    """
    Gets all details of the given subcategory 
    
    :param subCategoryObj:Holds the id of the string.Contains the following field,
                                                     id
    :type subCategoryObj: object                  
    :return SubCategory: return the subcategory
    """
    SubCategory = subCategoryDal.getSubCategory(subCategoryObj)
    return SubCategory

def editSubCategory(editSubCategoryObj):
    """
    update the subcategory information based on sub category id
    :param editCategoryObj: An object contains the following
                        id: Id of the subcategory
    :type editCategoryObj: object 
    
   
    """
    flag = subCategoryDal.editSubCategory(editSubCategoryObj)
    return flag
    
    
    
    