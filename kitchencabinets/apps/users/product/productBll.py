import productDal
def addCartList(cartObj):
    """
    add to cart list
    """
    productDal.addCartList(cartObj)
    
def listAllCartOfUser(cartObj):
    """
    cart list
    """
    return productDal.listAllCartOfUser(cartObj)
    
def checkUserCartForExistence(cartObj):
    """
    check for existence
    """
    return productDal.checkUserCartForExistence(cartObj)

def addToUserCart(cartObj):
    """
    adding to cart
    """
    
    productDal.addToUserCart(cartObj)


def getTheLastInsertedCartId():
    """
    get the last inserted cart_id
    """
    
    return productDal.getTheLastInsertedCartId()
def createOrderHistory(cartObj):
    """
    create order history
    """
    productDal.createOrderHistory(cartObj)

    
