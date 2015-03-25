import models
from apps.admin.common.models import Codes
from apps.admin.product.models import Product
from apps.admin.product import productBll



def filterSubCategories(subCategoryObj):
    """
    Gets all details of filtered in the database
    
    :return SubCategoriesList: All the SubCategories
    """
    FilteredSubCategoriesList = models.SubCategory.objects.filter(category=subCategoryObj.category,
                                                                  sub_category_status='active')
    return FilteredSubCategoriesList
   
def getAllSubCategories():
    """
    Gets all details of all the SubCategories in the database
    
    :return SubCategoriesList: All the SubCategories
    """
    SubCategoriesList = models.SubCategory.objects.all().only('category')
    return SubCategoriesList

def createSubCategory(subCategoryObj):
    
    """
    function is used to create the sub category
    
    """
    EXIST_FLAG = False
    category = models.Category.objects.get(id=subCategoryObj.category)
    #get the subcategory details using subcategoryname
    try:
        subCategoryDetails = models.SubCategory.objects.filter(sub_category_name=subCategoryObj.sub_category_name)
        print subCategoryDetails
        if subCategoryDetails:
            for cat in subCategoryDetails:
                if category == cat.category:
                    EXIST_FLAG = True
                    return EXIST_FLAG
    except:
        pass
    
    deatails = models.SubCategory(id=None,category=category,
                                       sub_category_status=subCategoryObj.sub_category_status,
                                       sub_category_name=subCategoryObj.sub_category_name
                                       )
    deatails.save()
    return EXIST_FLAG

def deleteSubCategory(deleteObj):

    """
    delete the  subcategory from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       subcategoryId
                      
    
  
    """
    
    productList = Product.objects.filter(sub_category=deleteObj.id)
    if(productList):
        for product in productList:
            try:
                productBll.deleteProducts(product)
            except:
                pass
            
    subCategory = models.SubCategory.objects.get(pk=deleteObj.id)
    try:
        subCategory.delete()
    except:
        pass
    

def getSubCategory(subCategoryObj):
    """
    Gets all details of the given subcategory 
    
    :param subCategoryObj:Holds the id of the string.Contains the following field,
                                                     id
    :type subCategoryObj: object                  
    :return SubCategory: return the SubCategory
    """
    SubCategory = models.SubCategory.objects.get(pk=subCategoryObj.id)
    return SubCategory


def editSubCategory(editSubCategoryObj):
    """
    update the category information based on subcategory id
    :param editSubCategoryObj: An object contains the following
                        category_id: Id of the subcategory
    :type editSubCategoryObj: object 
    
   
    """
    EXIST_FLAG = False
    category = models.Category.objects.get(id=editSubCategoryObj.category)
    editSubCategoryObj.id=str(editSubCategoryObj.id)
    
    #get the subcategory details using subcategoryname
    try:
        subCategoryDetails = models.SubCategory.objects.filter(sub_category_name=editSubCategoryObj.sub_category_name)
        if subCategoryDetails:
            for cat in subCategoryDetails:
                subId=str(cat.id)
                if category == cat.category and subId!=editSubCategoryObj.id:
                    EXIST_FLAG = True
                    return EXIST_FLAG
    except:
        pass
    
    subCategory = models.SubCategory.objects.get(pk=editSubCategoryObj.id) 
    subCategory.category=category
    subCategory.sub_category_name=editSubCategoryObj.sub_category_name
    subCategory.sub_category_status=editSubCategoryObj.sub_category_status
    subCategory.save()
    return EXIST_FLAG
    
