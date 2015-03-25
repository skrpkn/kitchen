from django.shortcuts import render_to_response
from django.template.context import RequestContext
from constants import Collection,DOOR_SUCCESS,DOOR_EXIST,DOOR_EDIT_SUCCESS,\
    LIST_COUNT
from django.contrib.auth.decorators import login_required, user_passes_test
import forms
from django.contrib import messages
from django.http import  HttpResponseRedirect
import doorBll
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from math import ceil

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listDoors(request):
    form = forms.DoorForm()
    DoorsList = doorBll.listDoors()
    DoorColorList = doorBll.listDoorColors()
    paginator = Paginator(DoorsList, LIST_COUNT)
    
    page = request.GET.get('page')
    if page == None :
        page=1
    
    try:
        doors = paginator.page(page)
    except PageNotAnInteger:
        doors = paginator.page(1)
        
    except EmptyPage:
        doors = paginator.page(paginator.num_pages)
        
        
    return render_to_response('admin/door/listDoors.html',{'form': form,'DoorColorList':DoorColorList,'DoorsList':doors},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createDoor(request):
    
    """
    function is used to create door
    """
    status = 'active'
    doorObj = Collection()
    form = forms.DoorForm()
    if request.method == 'POST':
        form = forms.DoorForm(request.POST)
        try:
            if form.is_valid():
                doorObj.door_name=request.POST['door_name']
                doorObj.door_price=request.POST['door_price']
                if "estimated_time" in request.POST and request.POST["estimated_time"]: 
                    doorObj.estimated_time = request.POST['estimated_time']
                else:
                    doorObj.estimated_time = 0
                    
                if "description" in request.POST and request.POST["description"]: 
                    doorObj.description = request.POST['description']
                else:
                    doorObj.description = ""
                    
                doorObj.door_id = doorBll.createDoor(doorObj)
                doorObj.color_count=request.POST['count']
                doorObj.color_count = int(doorObj.color_count)
                for count in range(doorObj.color_count):
                    count = count+1
                    count = str(count)
                    try:
                        
                        if "color_"+count in request.POST and request.POST["color_"+count]:    
                            doorObj.color = request.POST["color_"+count]
                            doorBll.createDoorColors(doorObj)
                    except:
                        pass
                messages.success(request, DOOR_SUCCESS)
                return HttpResponseRedirect('./')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, DOOR_EXIST)
    return render_to_response('admin/door/createDoors.html',{'form': form,'status':status},context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteDoor(request,doorId):
    """
    This Function is used to delete door
    
    :param request: It is an HttpRequest object
    :param doorId:It is the id of door
    """
    deleteObj = Collection()
    deleteObj.id=doorId
    doorBll.deleteDoor(deleteObj)
    return HttpResponseRedirect('/admin/door/list')

@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editDoor(request,doorId):
    status = ''
    params = {}
    doorObj = Collection()
    doorObj.id = doorId
    DoorInfo = doorBll.getDoor(doorObj)
    DoorColors = doorBll.getDoorColors(doorObj)
    DoorColorCount = len(DoorColors)
    form =forms.DoorForm (initial={'door_id': doorObj.id,
                                       'door_name': DoorInfo.door_name,
                                       'door_price': DoorInfo.door_price,
                                       'estimated_time':DoorInfo.estimated_time,
                                       'description':DoorInfo.description
                                       })
    if request.method == 'POST':
        try:
            doorObj.door_price=request.POST['door_price']
            doorObj.door_name=request.POST['door_name']
            doorObj.door_name = str(doorObj.door_name)
            doorObj.door_name = str.lower(doorObj.door_name)
            if "estimated_time" in request.POST and request.POST["estimated_time"]: 
                doorObj.estimated_time = request.POST['estimated_time']
            else:
                doorObj.estimated_time = 0
                    
            if "description" in request.POST and request.POST["description"]: 
                doorObj.description = request.POST['description']
            else:
                doorObj.description = ""
            doorBll.editDoor(doorObj)
            doorBll.deleteDoorColors(doorObj)
            doorObj.color_count=request.POST['count']
            doorObj.color_count = int(doorObj.color_count)
            doorObj.door_id = doorObj.id
            for count in range(doorObj.color_count):
                count = count+1
                count = str(count)
                try:
                    
                    if "color_"+count in request.POST and request.POST["color_"+count]:    
                        doorObj.color = request.POST["color_"+count]
                        doorBll.createDoorColors(doorObj)
                except:
                    pass
            messages.success(request, DOOR_EDIT_SUCCESS)
            return HttpResponseRedirect('/admin/door/list')
        except Exception as e:
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, DOOR_EXIST)
                
    params = {
                  'form': form,
                  'status':status,
                  'DoorColorCount':DoorColorCount,
                  'DoorColors':DoorColors,
                  'flag':1
              }
    return render_to_response('admin/door/createDoors.html',params,context_instance=RequestContext(request))
  

