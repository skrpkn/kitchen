from django.contrib.auth.decorators import login_required
from apps.admin.product.forms import ProductForm
from apps.admin.product import productBll
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from constants import LIST_COUNT, Collection
from settings import IMAGE_FILE_PATH
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import  HttpResponseRedirect, HttpResponse
from apps.users.product.productBll import addCartList, listAllCartOfUser,\
    checkUserCartForExistence, addToUserCart, getTheLastInsertedCartId,\
    createOrderHistory
from django.views.decorators.csrf import csrf_exempt

def listProducts(request):
    """
    list all the products
    """
    form_product = ProductForm()
    Products = productBll.listProduct()
    product_images = productBll.listProductImages()
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
   
    return render_to_response('users/product/listProducts.html',{'form': form_product,
                                                                 'IMAGE_FILE_PATH':IMAGE_FILE_PATH,
                                                                 'ProductList':ProductList,
                                                                 'product_images':product_images},
                                                                 context_instance=RequestContext(request))
@login_required 
def addtocart(request,price,product_id):
    """
    cart list
    """
    product_dict = {}
    cartObj = Collection()
    cartObj.product_name = []
    if request.user.is_authenticated():
        cartObj.price = float(price)
        cartObj.product_id = product_id
        cartObj.user_id = request.user.id
        cartObj.product = productBll.listProduct({'id':cartObj.product_id})
        addCartList(cartObj)
        cartList = listAllCartOfUser(cartObj)
        for product_id in cartList:
            cartObj.product_id_temp = product_id
            product = productBll.listProduct({'id':cartObj.product_id_temp})
            cartObj.quantity = checkUserCartForExistence(cartObj)
            cartObj.quantity = int(cartObj.quantity)
            cartObj.total_price = (cartObj.quantity * cartObj.price)
            product_dict[cartObj.product_id_temp] = {'product_name':product.product_name,
                                                     'price':cartObj.price,
                                                     'quantity':cartObj.quantity,
                                                     'total_price':cartObj.total_price}
            cartObj.product_name.append(product.product_name)
    else:
        return HttpResponseRedirect('/login')
    return render_to_response('users/product/shoppingCart.html',
                              {'productList':cartObj,
                               'itemList':product_dict,
                               'cartList':cartList},
                              context_instance=RequestContext(request))

@login_required 
def shoppingcart(request):
    cartObj = Collection()   
    if request.method=='POST' and 'update' in request.POST:
        if 'count' in request.POST and request.POST['count']:   
            cartObj.count = request.POST['count'] 
            for x in range(int(cartObj.count)):
                qty = 'qty'+str(x)
                ids = 'ids'+str(x)
                cartObj.quantity = request.POST[qty] 
                cartObj.id = request.POST[ids] 
                session_list = request.session['cart']
                for val in session_list:
                    if val.id == cartObj.id:
                        if int(cartObj.quantity) == 0:
                            session_list.remove(val)
                        else:
                            val.quantity = cartObj.quantity
                            val.total_price = (int(val.quantity) * float(val.price))
            request.session['cart'] = session_list
            request.session.modified = True
    # emptying cart
    elif request.method=='POST' and 'empty' in request.POST:
        request.session['cart'] = []
        request.session.modified = True
    #do checkout and save to db and clear sessions
    elif request.method=='POST' and 'checkout' in request.POST:
        session_list = request.session['cart']
        cartObj.user_id = request.user
        cartObj.cart_id = getTheLastInsertedCartId()
        for val in session_list:
            cartObj.session_value = val
            addToUserCart(cartObj)
        createOrderHistory(cartObj)
        request.session['cart'] = []
        request.session.modified = True
    else:
        pass
    return render_to_response('users/product/shoppingCart.html',
                              context_instance=RequestContext(request))
    
def add_cart_to_session(request):
    flag = False
    cartObj = Collection()  
    userCartObj = Collection() 
    if 'pn' in request.POST and request.POST['pn']:    
        userCartObj.product_name = request.POST['pn'] 
        
    if 'cart' in request.POST and request.POST['cart']:    
        cart = request.POST['cart'] 
    else:
        return HttpResponse('error', mimetype="application/javascript")
    # split to array
    # [0]=> id, [1] => width, [2]=> height, [3] => depth, [4]=> price
    cartArr = cart.split('~')
    if len(cartArr) == 5:
        userCartObj.id = cartArr[0].replace('id:',"")
        userCartObj.width = cartArr[1].replace('w:',"")
        userCartObj.height = cartArr[2].replace('h:',"")
        userCartObj.depth = cartArr[3].replace('d:',"")
        userCartObj.price = cartArr[4].replace('p:',"")
    else:
        return HttpResponse('error', mimetype="application/javascript")
    
    # create session object     
    try:
        sessionlist = request.session['cart']
    except:
        sessionlist = []
        
    sessionTempList = []
    userCartObj.quantity = 1
    for data in sessionlist:
        if userCartObj.id == data.id:
            userCartObj.quantity = int(data.quantity) + 1
            flag = True
        else:
            sessionTempList.append(data)
    userCartObj.total_price = (int(userCartObj.quantity) * float(userCartObj.price))
    
    if flag:
        sessionTempList.append(userCartObj)
        request.session['cart'] = sessionTempList
    else:
        sessionlist.append(userCartObj)
        request.session['cart'] = sessionlist
    request.session.modified = True
    return HttpResponse(1, mimetype="application/javascript")
    
@csrf_exempt
def deleteCartProduct(request):
    """
    delet a product from cart
    """
    if 'id' in request.POST and request.POST['id']:    
        product_sub_id = request.POST['id']
        session_list = request.session['cart']
        for val in session_list:
            if val.id == product_sub_id:
                session_list.remove(val)
        request.session['cart'] = session_list
        request.session.modified = True

    return HttpResponse(1, mimetype="application/javascript")
