import models
from apps.admin.common.models import Codes
from apps.admin.subCategory.models import SubCategory
from apps.admin.product.models import Product
from apps.admin.product import productBll

def createCategory(categoryObj):
    
    """
    function is used to create the category
    """
    try:
        category_image=categoryObj.image.name
    except:
        category_image = None
    categoryDeatails = models.Category(id=None,category_name=categoryObj.category_name,
                                       category_status=categoryObj.category_status,
                                       category_order=categoryObj.category_order,
                                       category_image=category_image
                                       )
    categoryDeatails.save()
    
    
def listCategories():
    """
    Gets all details of all the categories in the database
    
    :return CategoriesList: All the categories
    """
        
    CategoriesList = models.Category.objects.all().order_by('category_order')
    return CategoriesList

def listAllActiveCategories():
    """
    Gets all details of all the active categories in the database
    
    :return CategoriesList: All the active categories
    """
    CategoriesList = models.Category.objects.filter(category_status='active')
    return CategoriesList

def totalCategories():
    """
    Gets all details of all the categories in the database
    
    :return CategoriesList: All the categories
    """
    CategoriesCount = models.Category.objects.count();
    return CategoriesCount

def getCategory(categoryObj):
    """
    Gets all details of the given category 
    
    :param categoryObj:Holds the id of the string.Contains the following field,
                                                     id
    :type categoryObj: object                  
    :return category: return the category
    """
    category = models.Category.objects.get(pk=categoryObj.id)
    return category

def getCodesByGroupName(groupName):
    
    """
    """

    statusList = Codes.objects.filter(code_group=groupName).order_by('id')
    return statusList

def editCategory(editCategoryObj):
    """
    update the category information based on category id
    :param editCategoryObj: An object contains the following
                        category_id: Id of the category
    :type editCategoryObj: object 
    
   
    """
    
    category = models.Category.objects.get(pk=editCategoryObj.id) 
    try:
        category.category_image=editCategoryObj.image.name
    except:
        pass
    category.category_name=editCategoryObj.category_name
    category.category_status=editCategoryObj.category_status
    category.save()


def reorderCategory(reorderCategoryObj):
    """
    update the category information based on category id
    :param editCategoryObj: An object contains the following
                        category_id: Id of the category
    :type editCategoryObj: object 
    
   
    """

    category = models.Category.objects.get(pk=reorderCategoryObj.id) 
    category.category_order=reorderCategoryObj.category_order
    category.save()
    
    
def deleteCategory(deleteObj):

    """
    delete the  category from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       categoryId
                      
    
  
    """
    productList = Product.objects.filter(category=deleteObj.id)
    if(productList):
        for product in productList:
            try:
                productBll.deleteProducts(product)
            except:
                pass
    subCategories = SubCategory.objects.filter(category=deleteObj.id) 
    try:
        subCategories.delete()
    except:
        pass
    category = models.Category.objects.get(pk=deleteObj.id)
    try:
        category.delete()
    except:
        pass

