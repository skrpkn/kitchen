from django.contrib.auth.decorators import login_required, user_passes_test
import forms
from apps.admin.tax import taxBll
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from constants import Collection, TAX_SUCCESS, TAX_EXISTS, TAX_EDIT_SUCCESS
from django.contrib import messages
from django.http import HttpResponseRedirect
import datetime


@user_passes_test(lambda u: u.is_superuser)
@login_required 
def listTax(request):
    form = forms.TaxForm()
    taxList = taxBll.listAllTax()
    return render_to_response('admin/tax/listTax.html',{'form': form,'taxList':taxList},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createTax(request):
    
    """
    function is used to create the tax
    """
    status = 'active'
    taxObj = Collection()
    form = forms.TaxForm()
    
    if request.method == 'POST':
        form = forms.TaxForm(request.POST)
        try:
            #if form.is_valid():
                taxObj.tax_name=request.POST['tax_name']
                #taxObj.tax_date=request.POST['tax_date']
                taxObj.tax_date = datetime.date.today()
                taxObj.tax_status=request.POST['tax_status']
                taxObj.tax_rate=request.POST['tax_rate']
                taxBll.createTaxes(taxObj)
                messages.success(request, TAX_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, TAX_EXISTS)
    return render_to_response('admin/tax/createTax.html',{'form': form,'status':status},context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editTax(request,taxId):
    status = ''
    taxObj = Collection()
    taxObj.id= taxId
    taxList = taxBll.getTax(taxObj)
    print taxList.tax_rate
    form =forms.TaxForm (initial={'id': taxList.id,
                                       'tax_name': taxList.tax_name,
                                       'tax_status': taxList.tax_status,
                                       'tax_rate':taxList.tax_rate,
                                       })
    status = taxList.tax_status
    if request.method == 'POST':
        try:
            taxObj.tax_name=request.POST['tax_name']
            taxObj.tax_status=request.POST['tax_status']
            taxObj.tax_rate=request.POST['tax_rate']
            #taxObj.tax_date=request.POST['tax_date']
            taxObj.tax_date = datetime.date.today()
            taxBll.editTax(taxObj)
            messages.success(request, TAX_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/tax/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, TAX_EXISTS)
    return render_to_response('admin/tax/createTax.html',{'flag':1,'form': form,'status':status},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteTax(request,taxId):
    """
    This Function is used to delete a tax
    
    :param request: It is an HttpRequest object
    :param taxId:It is the id of tax
    """
    deleteObj = Collection()
    deleteObj.id=taxId
    taxBll.deleteTax(deleteObj)
    return HttpResponseRedirect('/admin/tax/list')

