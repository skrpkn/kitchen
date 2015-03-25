from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required, user_passes_test
from constants import Collection, LIST_COUNT, DRAWER_SUCCESS, DRAWER_EXISTS,\
    DRAWER_EDIT_SUCCESS
from django.http import HttpResponseRedirect
import forms
from django.contrib import messages
import drawersBll
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listDrawers(request):
    form = forms.DrawersForm()
    drawersList = drawersBll.listDrawers()
    
    paginator = Paginator(drawersList, LIST_COUNT)
    
    page = request.GET.get('page')
    if page == None :
        page=1
    
    try:
        drawers = paginator.page(page)
    except PageNotAnInteger:
        drawers = paginator.page(1)
        
    except EmptyPage:
        drawers = paginator.page(paginator.num_pages)
        
    return render_to_response('admin/drawers/listDrawers.html',{'form': form,'drawersList':drawers},context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createDrawers(request):
    
    """
    function is used to create the drawers
    """
    drawersObj = Collection()
    form = forms.DrawersForm()
    if request.method == 'POST':
        form = forms.DrawersForm(request.POST)
        try:
            if form.is_valid():
                drawersObj.drawer_name=request.POST['drawer_name']
                drawersObj.drawer_name = str(drawersObj.drawer_name)
                drawersObj.drawer_name = str.lower(drawersObj.drawer_name)
                drawersObj.drawer_unit_price = request.POST['drawer_unit_price'];
              
                drawersBll.createDrawers(drawersObj)
                messages.success(request, DRAWER_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, DRAWER_EXISTS)
    return render_to_response('admin/drawers/createDrawers.html',{'form': form},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editDrawers(request,drawersId):
    drawersObj = Collection()
    drawersObj.id= drawersId
    drawersList = drawersBll.getDrawers(drawersObj)
    form =forms.DrawersForm (initial={'id': drawersObj.id,
                                       'drawer_name': drawersList.drawer_name,
                                       'drawer_unit_price': drawersList.drawer_unit_price,
                                       })
    if request.method == 'POST':
        try:
            drawersObj.drawer_name=request.POST['drawer_name']
            drawersObj.drawer_unit_price=request.POST['drawer_unit_price']
            drawersObj.drawer_name = str(drawersObj.drawer_name)
            drawersObj.drawer_name = str.lower(drawersObj.drawer_name)
            drawersBll.editDrawers(drawersObj)
            messages.success(request,DRAWER_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/drawers/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, DRAWER_EXISTS)
    return render_to_response('admin/drawers/createDrawers.html',{'form': form,'flag':1},context_instance=RequestContext(request))
 
@user_passes_test(lambda u: u.is_superuser)
@login_required   
def deleteDrawers(request,drawersId):
    """
    This Function is used to delete drawers
    
    :param request: It is an HttpRequest object
    :param drawersId:It is the id of drawers
    """
    deleteObj = Collection()
    deleteObj.id=drawersId
    drawersBll.deleteDrawers(deleteObj)
    return HttpResponseRedirect('/admin/drawers/list')

