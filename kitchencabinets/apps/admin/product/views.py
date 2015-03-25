from django.shortcuts import render_to_response
from django.template.context import RequestContext
from constants import Collection,PRODUCT_SUCCESS,PRODUCT_EXIST, LIST_COUNT,\
     PRODUCT_EDIT_SUCCESS, ADMIN
from django.contrib.auth.decorators import login_required, user_passes_test
import forms
from django.contrib import messages
from django.http import  HttpResponseRedirect, HttpResponse
import productBll
from apps.admin.category import categoryBll
from apps.admin.subCategory import subCategoryBll
from apps.admin.hinges.forms import HingesForm, ProductHinges
from apps.admin.hinges import hingesBll
from apps.admin.door.forms import DoorForm, ProductDoorForm
from apps.admin.door import doorBll
from apps.admin.cabinet.forms import CabinetForm, ProductCabinet
from apps.admin.cabinet import cabinetBll
from settings import IMAGE_FILE_PATH, MEDIA_URL
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
from apps.admin.drawers.forms import DrawersForm, ProductDrawersForm
from apps.admin.drawers import drawersBll
from apps.admin.tax import taxBll
from itertools import chain
from apps.admin.common import commonBll
from django.views.decorators.csrf import csrf_exempt
from apps.admin.materials import materialBll
@csrf_exempt
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteProductImages(request):
    """
    delet an image
    """
    productObj = Collection()
    if 'id' in request.POST and request.POST['id']:    
        productObj.image_id = request.POST['id']
    else:
        return
    productBll.deleteProductImages(productObj)
    return HttpResponse('1', mimetype="application/javascript")

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def createProduct(request):
    
    """
    function is used to create a product
    """
    
    hinge= 'No'
    
    door= 'No'
    drawer = 'No'
    is_custom = 'No'
    #dictionary for hinges,cabinet,drawer
    cabinetDict={}
    hingesDict={}
    drawerDict={}
    taxDict = {}
    taxList = {}
    doorDict = {}
    listAllMaterials = listAllCabinets = {}
    
    #objects
    productObj = Collection()
    hingesObj = Collection()
    doorObj = Collection()
   
    #forms
    form_drawer = DrawersForm()
    form_product_drawer = ProductDrawersForm()
    form_product = forms.ProductForm()
    form_hinges = HingesForm()
    form_door = DoorForm()
    form_product_hinges = ProductHinges()
    form_product_doors = ProductDoorForm()
    
    form_cabinet = CabinetForm()
    form_product_cabinet = ProductCabinet()
    #list and count
    listAllDrawers = drawersBll.listDrawers()
    listAllCabinets =  cabinetBll.listCabinet()
    cabinetCount = len(listAllCabinets)
    
    drawersCount = listAllDrawers.count()
    listAllHinges = hingesBll.listHinges()
    hingesCount = listAllHinges.count()

    listAllDoors = doorBll.listDoors()
    doorsCount = len(listAllDoors)
    listAllCategory = categoryBll.listAllActiveCategories()
    # return only active materials
    params = {'status':'active'}
    listAllMaterials = materialBll.listMaterials(params)
    #listAllTax = taxBll.listAllTax()
    listAllTax = taxBll.listAlActivelTax()
    if request.method == 'POST':
        try:
            form_product = forms.ProductForm(request.POST,request.FILES)
            
            try:
                productObj.drawers=request.POST['is_drawer']
            except:
                productObj.drawers='No'
            try:
                productObj.hinges=request.POST['is_hinges']
            except:
                productObj.hinges='No'
            try:
                productObj.door=request.POST['is_door']
            except:
                productObj.door='No'
                
            if 'cabinet' in request.POST and request.POST['cabinet']:    
                productObj.cabinet = request.POST['cabinet']
                    
            #form for product
            productObj.category=request.POST['category_name']
            try:
                productObj.sub_category=request.POST['sub_category_name']
            except:
                productObj.sub_category = None
            productObj.product_name=request.POST['product_name']
            #productObj.product_code=request.POST['product_code']
            productObj.short_description=request.POST['short_description']
            productObj.descriptions=request.POST['descriptions']
            productObj.product_price=request.POST['product_price']
            
            
            productObj.min_height=request.POST['min_height']
            productObj.max_height=request.POST['max_height']
            productObj.min_height = float(productObj.min_height)
            productObj.max_height = float(productObj.max_height)
            if productObj.min_height > productObj.max_height:
                productObj.max_height = productObj.min_height
            productObj.height_scale=request.POST['height_scale']
            productObj.min_width=request.POST['min_width']
            productObj.max_width=request.POST['max_width']
            productObj.min_width = float(productObj.min_width)
            productObj.max_width = float(productObj.max_width)
            if productObj.min_width > productObj.max_width:
                productObj.max_width = productObj.min_width
            productObj.width_scale=request.POST['width_scale']
            productObj.min_depth=request.POST['min_depth']
            productObj.max_depth=request.POST['max_depth']
            productObj.min_depth = float(productObj.min_depth)
            productObj.max_depth = float(productObj.max_depth)
            if productObj.min_depth > productObj.max_depth:
                productObj.max_depth = productObj.min_depth
            productObj.depth_scale=request.POST['depth_scale']
#             try:
#                 productObj.image=request.FILES['image']
#                 categoryBll.uploadImage(productObj)
#             except:
#                     pass
            if 'is_custom' in request.POST and request.POST['is_custom']:    
                productObj.is_custom = request.POST['is_custom']
            if 'video' in request.POST and request.POST['video']:    
                productObj.video_url = request.POST['video']
            if 'discount' in request.POST and request.POST['discount']:    
                productObj.discount = request.POST['discount']   
            if 'material' in request.POST and request.POST['material']:    
                productObj.material_id = request.POST['material']
            product_id = productBll.createProduct(productObj)
            # add images
            productObj.image_count=request.POST['count']
            productObj.image_count = int(productObj.image_count)
            productObj.id = product_id
            for count in range(productObj.image_count):
                    count = count+1
                    count = str(count)
                    try:
                        productObj.image=request.FILES["photo_"+count]
                        productObj.description=request.POST["caption_"+count]
                        if productObj.image:
                            productObj.image_for = 'product/'
                            productObj.filePath = commonBll.uploadImage(productObj)
                            
                            productBll.createProductImages(productObj)
                    except:
                        pass
            # map tax section with products
            if 'tax_name' in request.POST and request.POST['tax_name']:
                taxList = request.POST.getlist('tax_name') 
                taxDict['product_id']=product_id
                for tax in taxList:
                    taxDict['tax_id']= tax
                    try:
                        taxBll.taxMapping(taxDict)
                    except:
                        pass
            #form for cabinet
            cabinetDict['product_id']=product_id
            for x in xrange(cabinetCount):
                    cabinet_id ='cabinetid'+str(x)
                    size='cabinet_size'+str(x)
                    cabinetDict['cabinet_id']=request.POST[cabinet_id]
                    cabinetDict['size'] =request.POST[size]
                    if(not cabinetDict['size']):
                        cabinetDict['size'] = 0
                    cabinetBll.createProductCabinet(cabinetDict)        
            #form for drawers
            form_drawer = DrawersForm(request.POST)
            if productObj.drawers=='Yes':
                drawerDict['product_id']=product_id
                for x in xrange(drawersCount):
                    drawer_id ='drawerid'+str(x)
                    drawer_name='drawername'+str(x)
                    drawer_qty='drawerqty'+str(x)
                    drawer_total_price='drawerprice'+str(x)
                    drawerDict['drawer_id']=request.POST[drawer_id]
                    drawerDict['drawer_qty'] =request.POST[drawer_qty]
                    if(not drawerDict['drawer_qty']):
                        drawerDict['drawer_qty'] = 0
                    # NEED TO CHANGE
                    #drawerDict['drawer_total_price'] =request.POST[drawer_total_price]
                    drawerDict['drawer_total_price'] = 0
                    drawersBll.createProductDrawers(drawerDict)
            #form for hinges
            form_hinges = HingesForm(request.POST)
            if productObj.hinges=='Yes':
                hingesDict['product_id']=product_id
                for x in xrange(hingesCount):
                    hinges_id ='hingesid'+str(x)
                    hinges_min='hingesmin'+str(x)
                    hinges_max='hingesmax'+str(x)
                    hingesDict['hinges_id']=request.POST[hinges_id]
                    hinges_min =request.POST[hinges_min]
                    if(not hinges_min):
                        hinges_min = 0
                    hinges_max =request.POST[hinges_max]
                    if(not hinges_max):
                        hinges_max = 0
                    if hinges_min > hinges_max:
                        hinges_max = hinges_min
                    hingesDict['minimum'] =  hinges_min
                    hingesDict['maximum'] = hinges_max 
                    hingesBll.createProductHinges(hingesDict)
                #hingesObj.hinges_unit_price = request.POST['hinges_unit_price']; 
            #form for doors
            form_door = DoorForm(request.POST)
            if productObj.door=='Yes':
                print "door"
                doorDict['product_id']=product_id
                for x in xrange(doorsCount):
                    door_id ='doorid'+str(x)
                    door_piece='pieces_count'+str(x)
                    doorDict['door_id']=request.POST[door_id]
                    doorDict['door_piece'] =request.POST[door_piece]
                    if(not doorDict['door_piece']):
                            doorDict['door_piece'] = 0
                    doorBll.createProductDoor(doorDict)  
            messages.success(request, PRODUCT_SUCCESS)
            return HttpResponseRedirect('./')
        except Exception as e:
            print e
            error = e.__class__.__name__
            if error == 'IntegrityError':
                messages.warning(request, PRODUCT_EXIST)
    return render_to_response('admin/product/createProducts.html',{'drawer':drawer,'hinge':hinge,'door':door,
                            'form_product_hinges':form_product_hinges,'form_product_drawer':form_product_drawer,
                            'form_product_doors':form_product_doors,
                            'form_door':form_door,'form_hinges':form_hinges,'form_drawer':form_drawer,
                            'form_product_cabinet':form_product_cabinet,
                            'form_cabinet':form_cabinet,
                            'form_product': form_product,'listAllHinges':listAllHinges,
                            'listAllTax':listAllTax,'doorsCount':doorsCount,
                            'listAllDoors':listAllDoors,'listAllDrawers':listAllDrawers,
                            'listAllCategory':listAllCategory,'SubCategoriesList':'','subcategoryCount':0,
                            'listAllMaterials':listAllMaterials,
                            'cabinet':'',
                            'is_custom':is_custom,
                            'listAllCabinets':listAllCabinets,
                            
                            },
                              context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def listProducts(request):
    """
    list all the products
    """
    form_product = forms.ProductForm()
    Products = productBll.listProduct()
    paginator = Paginator(Products, LIST_COUNT)
    
    page = request.GET.get('page')
    if page == None :
        page=1
    
    try:
        ProductList = paginator.page(page)
    except PageNotAnInteger:
        ProductList = paginator.page(1)
    except EmptyPage:
        ProductList = paginator.page(paginator.num_pages)
    return render_to_response('admin/product/listProducts.html',{'form': form_product,'IMAGE_FILE_PATH':IMAGE_FILE_PATH,'ProductList':ProductList},context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_superuser)
@login_required                                                                                
def viewProducts(request, productId):
    """
    product details
    """
    hingesList = doorList = drawersList = taxList = {}
   
    form_product = forms.ProductForm()
    productObj = Collection()
    productObj.id= productId
    product = productBll.getProduct(productObj)
    product_image_list = productBll.getProductImages(productObj)
    if product.is_hinges == 'Yes':
        hingesList = hingesBll.getProductHinges(productObj)
    if product.is_door == 'Yes':
        doorList = doorBll.getProductDoor(productObj)
    # get mapped tax
    taxList = taxBll.getProductTaxes(productObj)
    if product.is_drawer == 'Yes':
        drawersList = drawersBll.getProductDrawers(productObj)
    return render_to_response('admin/product/viewProducts.html',{'form': form_product, 
                    'IMAGE_FILE_PATH':IMAGE_FILE_PATH,'product':product,'hingesList':hingesList,'doorList':doorList,
                    'drawersList':drawersList,'product_image_list':product_image_list,
                    'taxList':taxList
                    },context_instance=RequestContext(request))
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def deleteProduct(request,productId):
    """
    This Function is used to delete a product, Corresponding product_hinges or Product_door or product_cabinet will
        be deleted
    
    :param request: It is an HttpRequest object
    :param productId:It is the id of product
    """
    deleteObj = Collection()
    deleteObj.id=productId
    productBll.deleteProducts(deleteObj)
    return HttpResponseRedirect('/admin/product/list/')
@user_passes_test(lambda u: u.is_superuser)
@login_required 
def editProduct(request,productId):
    
    """
    used to edit the subcategory
    """
    drawersCount = 0
    hingesCount = 0
    cabinetCount = 0
    subcategoryCount = 0
    drawerDict={}
    hingesDict={}
    cabinetDict={}
    taxDict = {}
    doorDict = {}
    listAllMaterials = {}
    listAllDrawers = listAllHinges = listAllTax = {}
    productDrawerList=''
    productCabinetList=''
    hingesList=''
    drawersList=''
    door_id=''
    drawer = 'No'
    hinge= 'No'
    is_custom = 'No'
    door= 'No'
    cabinet =''
    form_drawer = DrawersForm()
    form_product_drawer = ProductDrawersForm()
    form_product_hinges = ProductHinges()
    form_hinges = HingesForm()
    form_door = DoorForm()
    form_cabinet = CabinetForm()
    form_product_cabinet = ProductCabinet()
    doorObj = Collection()
    productObj = Collection()
    productObj.id= productId
    product_images=''
    product_images_count=0
    product_images = productBll.getProductImages(productObj)
    product_images_count = len(product_images)
    # get all product drawers details
    try:
        listAllDrawers = drawersBll.getAllProductDrawers(productObj)
    except:
        pass 
    drawersCount = len(listAllDrawers)
    try:
        listAllCabinets = cabinetBll.getAllProductCabinet(productObj)
    except:
        pass 
    cabinetCount = len(listAllCabinets)
    # get all hinges
    try:
        listAllHinges = hingesBll.getExcludeProductHinges(productObj)
    except:
        pass
    # get all hinges count
    hingesCount = len(listAllHinges)
    # get all doors
    try:
        #listAllDoors = doorBll.listDoors()
        listAllDoors = doorBll.getExcludeProductDoors(productObj)
    except:
        pass
    # get all hinges count
    doorsCount = len(listAllDoors)
    try:
        params = {'status':'active'}
        listAllMaterials = materialBll.listMaterials(params)
    except:
        pass
    product = productBll.getProduct(productObj)
    listAllCategory = categoryBll.listAllActiveCategories()
    SubCategoriesList = subCategoryBll.filterSubCategories(product)
    subcategoryCount = len(SubCategoriesList)
    category_id = product.category_id
    sub_category_id = product.sub_category_id
    material_id = product.material_id
    # get product tax details
    try:
        listAllTax = taxBll.getAllProductTaxes(productObj)
    except:
        pass
    #listAllTax = taxBll.listAllTax()
    if product.is_drawer == 'Yes':
        drawer= product.is_drawer
        try:
            drawersList = drawersBll.getProductDrawers(productObj)
        except:
            pass
    if product.is_hinges == 'Yes':
        hinge= product.is_hinges
        try:
            hingesList = hingesBll.getProductHinges(productObj)
        except:
            pass
    if product.is_door == 'Yes':
        door= product.is_door
        try:
            doorList = doorBll.getProductDoor(productObj)
            door_id = doorList.door.door_id
        except:
            pass
    if product.cabinet:
        cabinet = product.cabinet
    if product.is_custom:
        is_custom = product.is_custom
    #result = itertools.chain(productExcludeCabinet, productCabinetList)        
    form_product =forms.ProductForm (initial={'id': product.id,'product_name':product.product_name,
                                   'category': product.category,'sub_category':product.sub_category,'material': product.material,
                                   'product_code': product.product_code,'short_description':product.short_description,
                                   'descriptions': product.descriptions,'product_price':product.product_price,
                                   #'tax': product.tax,
                                   'min_height':product.min_height,
                                   'max_height': product.max_height,'height_scale':product.height_scale,
                                   'min_width': product.min_width,'max_width':product.max_width,
                                   'width_scale': product.width_scale,'min_depth':product.min_depth,
                                   'max_depth': product.max_depth,'depth_scale':product.depth_scale,
                                   'is_hinges': product.is_hinges,
                                   'is_door':product.is_door,
                                   'discount':product.discount,
                                   'video':product.video_url,
                                   'is_custom':is_custom
                                    })
    if request.method == 'POST':
        try:
            form_product = forms.ProductForm(request.POST,request.FILES)
            try:
                productObj.drawers=request.POST['is_drawer']
            except:
                productObj.drawers='No'
            try:
                productObj.hinges=request.POST['is_hinges']
            except:
                productObj.hinges='No'
            try:
                productObj.door=request.POST['is_door']
            except:
                productObj.door='No'
            try:
                productObj.image=request.FILES['image']
                categoryBll.uploadImage(productObj)
            except:
                    pass
            #form for product
            productObj.category=request.POST['category_name']
            try:
                productObj.sub_category=request.POST['sub_category_name']
            except:
                productObj.sub_category = None
            
            if 'cabinet' in request.POST and request.POST['cabinet']:    
                productObj.cabinet = request.POST['cabinet']
            productObj.product_name=request.POST['product_name']
            productObj.short_description=request.POST['short_description']
            productObj.descriptions=request.POST['descriptions']
            productObj.product_price=request.POST['product_price']
            productObj.min_height=request.POST['min_height']
            productObj.max_height=request.POST['max_height']
            productObj.min_height = float(productObj.min_height)
            productObj.max_height = float(productObj.max_height)
            if productObj.min_height > productObj.max_height:
                productObj.max_height = productObj.min_height
            productObj.height_scale=request.POST['height_scale']
            productObj.min_width=request.POST['min_width']
            productObj.max_width=request.POST['max_width']
            productObj.min_width = float(productObj.min_width)
            productObj.max_width = float(productObj.max_width)
            if productObj.min_width > productObj.max_width:
                productObj.max_width = productObj.min_width
            productObj.width_scale=request.POST['width_scale']
            productObj.min_depth=request.POST['min_depth']
            productObj.max_depth=request.POST['max_depth']
            productObj.min_depth = float(productObj.min_depth)
            productObj.max_depth = float(productObj.max_depth)
            if productObj.min_depth > productObj.max_depth:
                productObj.max_depth = productObj.min_depth
            productObj.depth_scale=request.POST['depth_scale']
            if 'discount' in request.POST and request.POST['discount']:    
                productObj.discount = request.POST['discount']   
            if 'video' in request.POST and request.POST['video']:    
                productObj.video_url = request.POST['video']
            if 'is_custom' in request.POST and request.POST['is_custom']:    
                productObj.is_custom = request.POST['is_custom']
            product_id = productBll.editProduct(productObj)
            # edit images
            productObj.image_count=request.POST['count']
            productObj.image_count = int(productObj.image_count)
            productObj.id = product_id
            for count in range(productObj.image_count):
                    count = count+1
                    count = str(count)
                    try:
                        productObj.image=request.FILES["photo_"+count]
                        productObj.description=request.POST["caption_"+count]
                        if productObj.image:
                            productObj.image_for = 'product/'
                            productObj.filePath = commonBll.uploadImage(productObj)
                            productBll.createProductImages(productObj)
                    except:
                        pass
            # map tax section with products
            if 'tax_name' in request.POST and request.POST['tax_name']:
                taxList = request.POST.getlist('tax_name') 
                taxDict['product_id']=product_id
                # delete all mapping
                try:
                    taxBll.deleteProductTax(taxDict)
                except:
                    pass
                for tax in taxList:
                    taxDict['tax_id']= tax
                    try:
                        taxBll.taxMapping(taxDict)
                    except:
                        pass
            #form for cabinet
            cabinetDict['product_id']=product_id
            try:
                cabinetBll.deleteProductCabinet(cabinetDict)
            except:
                pass
            for x in xrange(cabinetCount):
                    cabinet_id ='cabinetid'+str(x)
                    size='cabinet_size'+str(x)
                    cabinetDict['cabinet_id']=request.POST[cabinet_id]
                    cabinetDict['size'] =request.POST[size]
                    if(not cabinetDict['size']):
                        cabinetDict['size'] = 0
                    cabinetBll.createProductCabinet(cabinetDict)    
            form_drawer = DrawersForm(request.POST)
            drawerDict['product_id']=product_id
            try:
                drawersBll.deleteProductDrawer(drawerDict)
            except:
                pass
            if productObj.drawers=='Yes':
                for x in xrange(drawersCount):
                    drawer_id ='drawerid'+str(x)
                    drawer_qty='drawerqty'+str(x)
                    drawer_total_price='drawerprice'+str(x)
                    drawerDict['drawer_id']=request.POST[drawer_id]
                    drawerDict['drawer_qty'] =request.POST[drawer_qty]
                    if(not drawerDict['drawer_qty']):
                            drawerDict['drawer_qty'] = 0
                    # NEED TO cHANGE
                    #drawerDict['drawer_total_price'] =request.POST[drawer_total_price]
                    drawerDict['drawer_total_price'] = 0
                    drawersBll.createProductDrawers(drawerDict)
            form_hinges = HingesForm(request.POST)
            hingesDict['product_id']=product_id
            try:
                hingesBll.deleteProductHinges(hingesDict)
            except:
                pass
            if productObj.hinges=='Yes':
                for x in xrange(hingesCount):
                    hinges_id ='hingesid'+str(x)
                    hinges_min='hingesmin'+str(x)
                    hinges_max='hingesmax'+str(x)
                    hingesDict['hinges_id']=request.POST[hinges_id]
                    hinges_min =request.POST[hinges_min]
                    hinges_max =request.POST[hinges_max]
                    if(not hinges_min):
                        hinges_min = 0
                    if(not hinges_max):
                        hinges_max = hinges_min
                        
                    if hinges_min > hinges_max:
                        hinges_max = hinges_min
                    hingesDict['minimum'] =  hinges_min
                    hingesDict['maximum'] = hinges_max 
                    hingesBll.createProductHinges(hingesDict)
            #form for doors
            form_door = DoorForm(request.POST)
            doorDict['product_id']=product_id
            try:
                doorBll.deleteProductDoor(doorDict)
            except:
                pass
            if productObj.door=='Yes':
                doorDict['product_id']=product_id
                for x in xrange(doorsCount):
                    door_id ='doorid'+str(x)
                    door_piece='pieces_count'+str(x)
                    doorDict['door_id']=request.POST[door_id]
                    doorDict['door_piece'] =request.POST[door_piece]
                    if(not doorDict['door_piece']):
                            doorDict['door_piece'] = 0
                    doorBll.createProductDoor(doorDict)  
            messages.success(request, PRODUCT_EDIT_SUCCESS)       
            return HttpResponseRedirect('/admin/product/view/'+str(product_id))      
        except Exception as e:
            print e
            response = {}
            response['status']="error"
            response['errors']= e
            response=json.dumps(response)
            return HttpResponse(response) 
    return render_to_response('admin/product/createProducts.html',{'door_id':door_id,'drawer':drawer,'hinge':hinge,'door':door,
                                    'cabinet':cabinet,'flag':1,'form_door':form_door,'form_product': form_product,
                                    'form_drawer':form_drawer,'form_product_drawer':form_product_drawer,
                                    'form_hinges':form_hinges,'form_product_hinges':form_product_hinges,
                                    'form_product_cabinet':form_product_cabinet,
                                    'form_cabinet':form_cabinet,
                                    'hingesList':hingesList,
                                    'listAllDrawers':listAllDrawers,
                                    'listAllTax':listAllTax,
                                    'listAllHinges':listAllHinges,
                                    'product_images':product_images,
                                    'material_id':material_id,
                                    'product_images_count':product_images_count,
                                    'listAllCabinets':listAllCabinets,
                                    'listAllDoors':listAllDoors,'SubCategoriesList':SubCategoriesList,
                                    'listAllCategory':listAllCategory,'sub_category_id':sub_category_id,
                                    'listAllMaterials':listAllMaterials,
                                    'is_custom':is_custom,
                                    'category_id':category_id,'subcategoryCount':subcategoryCount},context_instance=RequestContext(request))
  




