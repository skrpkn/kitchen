from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from constants import Collection, CABINET_SUCCESS, CABINET_EXISTS, LIST_COUNT,\
    CABINET_EDIT_SUCCESS
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
import forms
import cabinetBll

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listCabinet(request):
    form = forms.CabinetForm()
    cabinetList = cabinetBll.listCabinet()
    paginator = Paginator(cabinetList, LIST_COUNT)
    page = request.GET.get('page')
    if page == None :
        page=1
    try:
        cabinets = paginator.page(page)
    except PageNotAnInteger:
        cabinets = paginator.page(1)
    except EmptyPage:
        cabinets = paginator.page(paginator.num_pages)
    return render_to_response('admin/cabinet/listCabinet.html',{'form': form,'cabinetsList':cabinets},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createCabinet(request):
    
    """
    function is used to create the category
    """
    cabinetList = []
    cabinetObj = Collection()
    form = forms.CabinetForm()
    if request.method == 'POST':
        form = forms.CabinetForm(request.POST)
        try:
            if form.is_valid():
                cabinetObj.cabinet_name=request.POST['cabinet_name']
                cabinetObj.cabinet_name = str(cabinetObj.cabinet_name)
                cabinetObj.cabinet_name = str.lower(cabinetObj.cabinet_name)
                if 'formula' in request.POST and request.POST['formula']:
                    cabinetObj.formulaList = request.POST.getlist('formula') 
                    formulaItems = cabinetBll.checkFormula(cabinetObj)
                    cabinetObj.width = formulaItems.width
                    cabinetObj.height = formulaItems.height
                    cabinetObj.depth = formulaItems.depth
                else:
                    cabinetObj.width=2
                    cabinetObj.height=2
                    cabinetObj.depth=2
                cabinetBll.createCabinet(cabinetObj)
                messages.success(request, CABINET_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, CABINET_EXISTS)
    return render_to_response('admin/cabinet/createCabinet.html',{'cabinetList':cabinetList,'form': form},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editCabinet(request,cabinetId):
    cabinetObj = Collection()
    cabinetObj.id= cabinetId
    cabinetList = cabinetBll.getCabinet(cabinetObj)
    form =forms.CabinetForm (initial={'id': cabinetObj.id,
                                       'cabinet_name': cabinetList.cabinet_name,
                                       })
    if request.method == 'POST':
        try:
            cabinetObj.cabinet_name=request.POST['cabinet_name']
            cabinetObj.cabinet_name = str(cabinetObj.cabinet_name)
            cabinetObj.cabinet_name = str.lower(cabinetObj.cabinet_name)
            if 'formula' in request.POST and request.POST['formula']:
                    cabinetObj.formulaList = request.POST.getlist('formula') 
                    formulaItems = cabinetBll.checkFormula(cabinetObj)
                    cabinetObj.width = formulaItems.width
                    cabinetObj.height = formulaItems.height
                    cabinetObj.depth = formulaItems.depth
            else:
                cabinetObj.width=2
                cabinetObj.height=2
                cabinetObj.depth=2
            cabinetBll.editCabinet(cabinetObj)
            messages.success(request, CABINET_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/cabinet/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, CABINET_EXISTS)
    return render_to_response('admin/cabinet/createCabinet.html',{'cabinetList':cabinetList,'form': form,'flag':1},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteCabinet(request,cabinetId):
    """
    This Function is used to delete cabinet
    
    :param request: It is an HttpRequest object
    :param hingesId:It is the id of hinges
    """
    try:
        deleteObj = Collection()
        deleteObj.id=cabinetId
        cabinetBll.deleteCabinet(deleteObj)
    except:
        pass
    return HttpResponseRedirect('/admin/cabinet/list')

