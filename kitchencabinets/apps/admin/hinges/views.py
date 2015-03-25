from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from constants import Collection, HINGES_SUCCESS,HINGES_EXISTS,\
    HINGES_EDIT_SUCCESS, LIST_COUNT
from django.http import HttpResponseRedirect
import forms
from django.contrib import messages
import hingesBll
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listHinges(request):
    form = forms.HingesForm()
    hingesList = hingesBll.listHinges()
    
    paginator = Paginator(hingesList, LIST_COUNT)
    
    page = request.GET.get('page')
    if page == None :
        page=1
    
    try:
        hinges = paginator.page(page)
    except PageNotAnInteger:
        hinges = paginator.page(1)
        
    except EmptyPage:
        hinges = paginator.page(paginator.num_pages)
        
    return render_to_response('admin/hinges/listHinges.html',{'form': form,'hingesList':hinges},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createHinges(request):
    
    """
    function is used to create the category
    """
    hingesObj = Collection()
    form = forms.HingesForm()
    if request.method == 'POST':
        form = forms.HingesForm(request.POST)
        try:
            if form.is_valid():
                hingesObj.hinges_name=request.POST['hinges_name']
                hingesObj.hinges_name = str(hingesObj.hinges_name)
                hingesObj.hinges_name = str.lower(hingesObj.hinges_name)
                hingesObj.hinges_unit_price = request.POST['hinges_unit_price'];
              
                hingesBll.createHinges(hingesObj)
                messages.success(request, HINGES_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, HINGES_EXISTS)
    return render_to_response('admin/hinges/createHinges.html',{'form': form},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editHinges(request,hingesId):
    hingesObj = Collection()
    hingesObj.id= hingesId
    hingesList = hingesBll.getHinges(hingesObj)
    form =forms.HingesForm (initial={'id': hingesObj.id,
                                       'hinges_name': hingesList.hinges_name,
                                       'hinges_unit_price': hingesList.hinges_unit_price,
                                       })
    if request.method == 'POST':
        try:
            hingesObj.hinges_name=request.POST['hinges_name']
            hingesObj.hinges_unit_price=request.POST['hinges_unit_price']
            hingesObj.hinges_name = str(hingesObj.hinges_name)
            hingesObj.hinges_name = str.lower(hingesObj.hinges_name)
            hingesBll.editHinges(hingesObj)
            messages.success(request, HINGES_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/hinges/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, HINGES_EXISTS)
    return render_to_response('admin/hinges/createHinges.html',{'form': form,'flag':1},context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required   
def deleteHinges(request,hingesId):
    """
    This Function is used to delete hinges
    
    :param request: It is an HttpRequest object
    :param hingesId:It is the id of hinges
    """
    deleteObj = Collection()
    deleteObj.id=hingesId
    hingesBll.deleteHinges(deleteObj)
    return HttpResponseRedirect('/admin/hinges/list')

