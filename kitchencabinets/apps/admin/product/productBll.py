import productDal


def createProduct(productObj):
    
    """
    function is used to create a product
    """
   
    #checking the field has a value, if not assigned a null value
    if not productObj.min_height:
        productObj.min_height=None
    if not productObj.max_height:
        productObj.max_height=None
    if not productObj.height_scale:
        productObj.height_scale=None
    if not productObj.min_width:
        productObj.min_width=None
    if not productObj.max_width:
        productObj.max_width=None
    if not productObj.width_scale:
        productObj.width_scale=None
    if not productObj.min_depth:
        productObj.min_depth=None
    if not productObj.max_depth:
        productObj.max_depth=None
    if not productObj.depth_scale:
        productObj.depth_scale=None
    try:
        if not productObj.video_url:
            productObj.video_url=None
    except:
        productObj.video_url=None
        pass
        
    try:
        if not productObj.discount:
            productObj.discount= 0
    except:
        productObj.discount= 0
        pass
    #using for future purpose, has to remove 
    
    product_id = productDal.createProduct(productObj)
    return product_id
def listProduct(params= []):
    """
    Gets all details of all the products in the database
    
    :return ProductList: All the products
    """
    ProductList = productDal.listProduct(params)
    return ProductList

def getProduct(productObj):
    """
    Gets details of a products in the database
    
    :return product: the products details
    """
    product = productDal.getProduct(productObj)
    return product

def getProductImages(productObj):
    """
    Gets details of all the images of a products in the database
    
    :return product_image: the image details
    """
    product_image = productDal.getProductImages(productObj)
    return product_image




def deleteProducts(deleteObj):
    
    """
    delete a product
    """
    productDal.deleteProducts(deleteObj)

def deleteProductImages(deleteObj):
    
    """
    delete all mapping images
    """
    productDal.deleteProductImages(deleteObj)


def editProduct(productObj):
    
    """
    function is used to edit a product
    """
    
    #checking the field has a value, if not assigned a null value
    if not productObj.min_height:
        productObj.min_height=None
    if not productObj.max_height:
        productObj.max_height=None
    if not productObj.height_scale:
        productObj.height_scale=None
    if not productObj.min_width:
        productObj.min_width=None
    if not productObj.max_width:
        productObj.max_width=None
    if not productObj.width_scale:
        productObj.width_scale=None
    if not productObj.min_depth:
        productObj.min_depth=None
    if not productObj.max_depth:
        productObj.max_depth=None
    if not productObj.depth_scale:
        productObj.depth_scale=None
    try:
        if not productObj.video_url:
            productObj.video_url=None
    except:
        productObj.video_url=None
        pass
    try:
        if not productObj.discount:
            productObj.discount= 0
    except:
        productObj.discount= 0
        pass    
    product_id = productDal.editProduct(productObj)
    return product_id


def createProductImages(productObj):
    """
    create the product images
    """
    productDal.createProductImages(productObj)





def listProductImages(params= []):
    """
    Gets all details of all the product images in the database
    
    :return imageList: All the product images
    """
    imageList = productDal.listProductImages(params)
    return imageList














