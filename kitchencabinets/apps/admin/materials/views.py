from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.contrib import messages
import forms
import materialBll
from constants import Collection, MATERIAL_SUCCESS, MATERIAL_EXISTS,\
    MATERIAL_EDIT_SUCCESS
from django.shortcuts import render_to_response


@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                 
def createMaterial(request):
    
    """
    function is used to create the materials
    """
    materialObj = Collection()
    form = forms.MaterialForm()
    status = 'active'
    if request.method == 'POST':
        form = forms.MaterialForm(request.POST)
        try:
            if form.is_valid():
                materialObj.name=request.POST['materials_name']
                materialObj.name = str(materialObj.name)
                materialObj.name = str.lower(materialObj.name)
                materialObj.description=request.POST['descriptions']
                materialObj.price=request.POST['materials_price']
                materialObj.status=request.POST['status']
                materialBll.createMaterial(materialObj)
                messages.success(request, MATERIAL_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, MATERIAL_EXISTS)
    return render_to_response('admin/materials/createMaterial.html',{'status':status,'form': form},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listMaterial(request):
    form = forms.MaterialForm()
    materialsList = materialBll.listMaterials()
    return render_to_response('admin/materials/listMaterials.html',{'form': form,'materialsList':materialsList},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editMaterial(request,materialId):
    status = ''
    materialObj = Collection()
    materialObj.id= materialId
    materailList = materialBll.listMaterials({'id':materialId})
    form =forms.MaterialForm (initial={'id': materailList.id,
                                       'materials_name': materailList.name,
                                       'materials_price': materailList.price,
                                       'descriptions': materailList.description,
                                       'status': materailList.status
                                       })
    status = materailList.status
    if request.method == 'POST':
        try:
            materialObj.name=request.POST['materials_name']
            materialObj.name = str(materialObj.name)
            materialObj.name = str.lower(materialObj.name)
            materialObj.status=request.POST['status']
            materialObj.price=request.POST['materials_price']
            materialObj.description=request.POST['descriptions']
            materialBll.editMaterial(materialObj)
            messages.success(request, MATERIAL_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/materials/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, MATERIAL_EXISTS)
    return render_to_response('admin/materials/createMaterial.html',{'status':status,'form': form,'flag':1,'materailList':materailList},context_instance=RequestContext(request))



@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteMaterials(request,materialId):
    """
    This Function is used to delete a meterial
    
    :param request: It is an HttpRequest object
    :param categoryId:It is the id of category
    """
    deleteObj = Collection()
    deleteObj.id=materialId
    materialBll.deleteMaterial(deleteObj)
    return HttpResponseRedirect('/admin/materials/list')


  