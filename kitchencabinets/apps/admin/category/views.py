from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.views.decorators.csrf import csrf_exempt
from constants import Collection, CATEGORY_EXISTS,CATEGORY_SUCCESS,\
    CATEGORY_EDIT_SUCCESS
from settings import  MEDIA_URL,IMAGE_FILE_PATH
from django.contrib.auth.decorators import login_required, user_passes_test
import categoryBll

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers 
from django.utils.datastructures import MultiValueDictKeyError 
import forms
from django.contrib import messages

import base64
import json
import os



@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listCategory(request):
    form = forms.CategoryForm()
    CategoriesList = categoryBll.listCategories()
    return render_to_response('admin/category/listCategory.html',{'form': form,'IMAGE_FILE_PATH':IMAGE_FILE_PATH,'CategoriesList':CategoriesList},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required  
@csrf_exempt                                                                              
def reorderCategory(request):
    form = forms.CategoryForm()
    CategoriesList = categoryBll.listCategories()
    if request.method == 'POST':
        categoryObj = Collection()
        string = request.POST['order']
            
        listingCounter = 1;
        updateRecordsArray = string.split('~')
        for item in updateRecordsArray:
            if item == '':
                continue
            categoryObj.category_order = listingCounter
            categoryObj.id = item
            categoryBll.reorderCategory(categoryObj)
            listingCounter = listingCounter+1
                
    return render_to_response('admin/category/reorderCategory.html',{'form': form,'CategoriesList':CategoriesList},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def createCategory(request):
    
    """
    function is used to create the category
    """
    status = 'active'
    categoryObj = Collection()
    form = forms.CategoryForm()
    
    if request.method == 'POST':
        form = forms.CategoryForm(request.POST,request.FILES)
        try:
            if form.is_valid():
                categoryObj.category_name=request.POST['category_name']
                currentCount = categoryBll.totalCategories();
                categoryObj.category_order = currentCount+1;
                categoryObj.category_status=request.POST['category_status']
                categoryObj.category_name = str(categoryObj.category_name)
                categoryObj.category_name = str.lower(categoryObj.category_name)
                try:
                    categoryObj.image = request.FILES['category_image']
                    categoryBll.uploadImage(categoryObj)
                except:
                    pass
                categoryBll.createCategory(categoryObj)
                messages.success(request, CATEGORY_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, CATEGORY_EXISTS)
    return render_to_response('admin/category/createCategory.html',{'form': form,'status':status},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteCategory(request,categoryId):
    """
    This Function is used to delete an category
    
    :param request: It is an HttpRequest object
    :param categoryId:It is the id of category
    """
    deleteObj = Collection()
    deleteObj.id=categoryId
    categoryBll.deleteCategory(deleteObj)
    return HttpResponseRedirect('/admin/category/list')
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editCategory(request,categoryId):
    status = ''
    categoryObj = Collection()
    categoryObj.id= categoryId
    categoryList = categoryBll.getCategory(categoryObj)
   # print "path",MEDIA_URL + '/'+categoryList.category_image
    form =forms.CategoryForm (initial={'id': categoryObj.id,
                                       'category_name': categoryList.category_name,
                                       'category_status': categoryList.category_status,
                                      # 'category_image': MEDIA_URL + '/'+categoryList.category_image
                                       })
    status = categoryList.category_status
    if request.method == 'POST':
        try:
            categoryObj.category_name=request.POST['category_name']
#             categoryObj.category_order=request.POST['category_order']
            categoryObj.category_status=request.POST['category_status']
            categoryObj.category_name = str(categoryObj.category_name)
            categoryObj.category_name = str.lower(categoryObj.category_name)
            try:
                categoryObj.image = request.FILES['category_image']
                categoryBll.uploadImage(categoryObj)
            except:
                pass
            categoryBll.editCategory(categoryObj)
            messages.success(request, CATEGORY_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/category/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, CATEGORY_EXISTS)
    return render_to_response('admin/category/createCategory.html',{'form': form,'status':status,'IMAGE_FILE_PATH':IMAGE_FILE_PATH,'flag':1,'category':categoryList},context_instance=RequestContext(request))
  



