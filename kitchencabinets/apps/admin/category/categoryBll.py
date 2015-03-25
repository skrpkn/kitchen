import categoryDal
from settings import MEDIA_URL


def createCategory(categoryObj):
    
    """
    function is used to create the category
    """
    categoryDal.createCategory(categoryObj)
    
def listCategories():
    """
    Gets all details of all the categories in the database
    
    :return CategoriesList: All the categories
    """
    CategoriesList = categoryDal.listCategories()
    return CategoriesList

def listAllActiveCategories():
    """
    Gets all details of all the categories in the database
    
    :return CategoriesList: All the categories
    """
    CategoriesList = categoryDal.listAllActiveCategories()
    return CategoriesList

def totalCategories():
    """
    Gets all details of all the categories in the database
    
    :return CategoriesList: All the categories
    """
    CategoriesTotal = categoryDal.totalCategories()
    return CategoriesTotal

def getCategory(categoryObj):
    """
    Gets all details of the given category 
    
    :param categoryObj:Holds the id of the string.Contains the following field,
                                                     id
    :type categoryObj: object                  
    :return category: return the category
    """
    category = categoryDal.getCategory(categoryObj)
    return category

def getCategoryStatus():
    
    """
   
        
    """
    statusList = categoryDal.getCodesByGroupName('category_status')
    return statusList

def editCategory(editCategoryObj):
    """
    update the category information based on category id
    :param editCategoryObj: An object contains the following
                        category_id: Id of the category
    :type editCategoryObj: object 
    
   
    """
    categoryDal.editCategory(editCategoryObj)


def reorderCategory(reorderCategoryObj):
    """
    update the category information based on category id
    :param editCategoryObj: An object contains the following
                        category_id: Id of the category
    :type editCategoryObj: object 
    
   
    """
    categoryDal.reorderCategory(reorderCategoryObj)

    
def deleteCategory(deleteObj):
    
    """
        
    """
    categoryDal.deleteCategory(deleteObj) 

def uploadImage(categoryObj):
    """
    """
    image = categoryObj.image
    categoryObj.filename=image.name    
    categoryObj.filePath=MEDIA_URL+'/category/'+categoryObj.filename             
    destination = open(categoryObj.filePath,'wb+')                               
    for chunk in image.chunks():                   
        destination.write(chunk)
        destination.close()  
