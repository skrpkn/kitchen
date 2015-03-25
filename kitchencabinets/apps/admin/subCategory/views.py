from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from constants import Collection, SUB_CATEGORY_SUCCESS,\
    SUB_CATEGORY_EXISTS_FOR_CATEGORY, SUB_CATEGORY_EDIT_SUCCESS, LIST_COUNT
from django.contrib.auth.decorators import login_required, user_passes_test
import subCategoryBll
from django.http import HttpResponse, HttpResponseRedirect
import forms
from django.contrib import messages
from settings import IMAGE_FILE_PATH, MEDIA_URL
import json
from apps.admin.category import categoryBll
from django.core.paginator import Paginator, EmptyPage,\
    PageNotAnInteger
from apps.admin.product.forms import ProductForm
from django.core import serializers


@user_passes_test(lambda u: u.is_superuser)
@login_required 
def filterSubCategory(request, cat_id):
    """
    get all subcategories of a category
    """
    subCategoryObj = Collection()
    subCategoryObj.category = cat_id
    json_subcat = serializers.serialize("json", subCategoryBll.filterSubCategories(subCategoryObj))
    return HttpResponse(json_subcat, mimetype="application/javascript")


@user_passes_test(lambda u: u.is_superuser)
@login_required     
def listSubCategory(request):
    """
    list all subcategory
    """
    form = forms.SubCategoryForm()
    SubCategoriesList = subCategoryBll.getAllSubCategories()
    paginator = Paginator(SubCategoriesList, LIST_COUNT)
    
    page = request.GET.get('page')
    if page == None :
        page=1
    
    try:
        subCategories = paginator.page(page)
    except PageNotAnInteger:
        subCategories = paginator.page(1)
    except EmptyPage:
        subCategories = paginator.page(paginator.num_pages)

    return render_to_response('admin/category/listSubCategory.html',{'form': form,'subCategories':subCategories,'IMAGE_FILE_PATH':IMAGE_FILE_PATH},context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createSubCategory(request):
    """
    function is used to create the createSubCategory
    """
    status = 'active'
    category_id = 0
    subCategoryObj = Collection()
    form = forms.SubCategoryForm()
    #listAllCategory = categoryBll.listCategories()
    listAllCategory = categoryBll.listAllActiveCategories()
    if request.method == 'POST':
        form = forms.SubCategoryForm(request.POST)
        try:
            subCategoryObj.category=request.POST['category_name']
            subCategoryObj.sub_category_name=request.POST['sub_category_name']
            subCategoryObj.sub_category_status=request.POST['sub_category_status']
            subCategoryObj.sub_category_name = str(subCategoryObj.sub_category_name)
            subCategoryObj.sub_category_name = str.lower(subCategoryObj.sub_category_name)
            flag = subCategoryBll.createSubCategory(subCategoryObj)
            if flag:
                messages.warning(request, SUB_CATEGORY_EXISTS_FOR_CATEGORY)
            else:
                messages.success(request, SUB_CATEGORY_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as exception:
            #response = {}
           # response['status']="error"
           # response['errors']= exception
           # response=json.dumps(response)
            print exception
            #return HttpResponse(response) 
    return render_to_response('admin/category/createSubCategory.html',{'form': form,'listAllCategory':listAllCategory,'category_id':category_id, 'status':status},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteSubCategory(request,subCategoryId):
    """
    This Function is used to delete a sub category
    
    :param request: It is an HttpRequest object
    :param categoryId:It is the id of sub category
    """
    deleteObj = Collection()
    deleteObj.id=subCategoryId
    subCategoryBll.deleteSubCategory(deleteObj)
    return HttpResponseRedirect('/admin/subcategory/list/')

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editSubCategory(request,subCategoryId):
    
    """
    used to edit the subcategory
    """
    status = ''
    category_id = 0
    subCategoryObj = Collection()
    subCategoryObj.id= subCategoryId
    listAllCategory = categoryBll.listAllActiveCategories()
    subCategoryDetails = subCategoryBll.getSubCategory(subCategoryObj)
    form =forms.SubCategoryForm (initial={'id': subCategoryObj.id,'category':subCategoryDetails.category,
                                       'sub_category_name': subCategoryDetails.sub_category_name,
                                       'sub_category_status': subCategoryDetails.sub_category_status})
    status = subCategoryDetails.sub_category_status
    category_id = subCategoryDetails.category_id
    if request.method == 'POST':
        try:
            subCategoryObj.category=request.POST['category_name']
            subCategoryObj.sub_category_name=request.POST['sub_category_name']
            subCategoryObj.sub_category_status=request.POST['sub_category_status']
            
            flag = subCategoryBll.editSubCategory(subCategoryObj)
            if flag:
                messages.warning(request, SUB_CATEGORY_EXISTS_FOR_CATEGORY)
            else:
                messages.success(request, SUB_CATEGORY_EDIT_SUCCESS)
                return HttpResponseRedirect('/admin/subcategory/list/')
        except Exception as e:
            response = {}
            response['status']="error"
            response['errors']= e
            response=json.dumps(response)
            return HttpResponse(response) 
    return render_to_response('admin/category/createSubCategory.html',{'flag':1,'form': form,'listAllCategory':listAllCategory,'status':status,'category_id':category_id},context_instance=RequestContext(request))
  

