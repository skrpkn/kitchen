import models

from django.contrib.auth.models import User
def addCartList(cartObj):
    """
    add to cart list
    """
    #checking the user is already added the product into the cart
    
    
    cartObj.user = User.objects.get(id=cartObj.user_id)
    cartList = models.ShopingCart(id=None,user=cartObj.user,product=cartObj.product)
    cartList.save()
    
    
def checkUserCartForExistence(cartObj):
    """
    check for existence
    """
    cartList = models.ShopingCart.objects.filter(user=cartObj.user_id,product=cartObj.product_id_temp)
    return len(cartList)

def listAllCartOfUser(cartObj):
    """
    cart list
    """
    cartList = models.ShopingCart.objects.filter(user=cartObj.user_id).distinct() 
    return cartList

def getTheLastInsertedCartId():
    """
    get the last inserted cart_id
    """
    try:
        last_val = models.Cart.objects.latest('cart_id')
        cart_id = int(last_val.cart_id)+1
    except:
        cart_id = 1
    return cart_id

def addToUserCart(cartObj):
    """
    adding to cart
    """

    cartList = models.Cart(id=None,
                           cart_id=cartObj.cart_id,
                           product_id=cartObj.session_value.id,
                           user=cartObj.user_id,
                           width=cartObj.session_value.width,
                           height=cartObj.session_value.height,
                           depth=cartObj.session_value.depth,
                           price=cartObj.session_value.price,
                           quantity=cartObj.session_value.quantity)
    cartList.save()
    
def createOrderHistory(cartObj):
    """
    create order history
    """
    cartList = models.OrderHistory(id=None,cart_id=cartObj.cart_id,check_out=1)
    cartList.save()

    
    