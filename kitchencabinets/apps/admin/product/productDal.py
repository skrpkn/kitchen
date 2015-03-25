import models
from apps.admin.door.models import ProductDoors
from apps.admin.cabinet.models import ProductCabinetConstruction
from apps.admin.hinges.models import ProductHinges
from apps.admin.tax.models import TaxMapping
from apps.admin.product.models import ImageMapping

def createProduct(productObj):
    
    """
    function is used to create a product
    """
    category = models.Category.objects.get(id=productObj.category)
    material_id = models.Materials.objects.get(id=productObj.material_id)
    #tax = Tax.objects.get(id=productObj.tax)
    #print "tax",tax
    if not productObj.sub_category:
        sub_category=None
    else:
        sub_category = models.SubCategory.objects.get(id=productObj.sub_category)
    try:
        product_image=productObj.image.name
    except:
        product_image = None
    productDeatails = models.Product(
                                    id=None,
                                    cabinet = productObj.cabinet,
                                    material=material_id,
                                    category=category,
                                    sub_category=sub_category,
                                    product_name=productObj.product_name,
                                    #product_code=productObj.product_code,
                                    short_description=productObj.short_description,
                                    descriptions=productObj.descriptions,
                                    product_price=productObj.product_price,
                                    #tax=tax,
                                    min_height=productObj.min_height,
                                    max_height=productObj.max_height,
                                    height_scale=productObj.height_scale,
                                    min_width=productObj.min_width,
                                    max_width=productObj.max_width,
                                    width_scale=productObj.width_scale,
                                    min_depth=productObj.min_depth,
                                    max_depth=productObj.max_depth,
                                    depth_scale=productObj.depth_scale,
                                    is_hinges=productObj.hinges,
                                    image=product_image,
                                    is_door=productObj.door,
                                    is_drawer=productObj.drawers,
                                    video_url = productObj.video_url,
                                    discount = productObj.discount ,
                                    is_custom = productObj.is_custom,
                                    )
    productDeatails.save()
    product_id = productDeatails.id
    return product_id

def createProductImages(productObj):
    """
    create the product images
    """
    product = getProduct(productObj)
    productImageDeatails = models.ImageMapping(id=None,product=product,image_path=productObj.filePath,
                                               description=productObj.description)
    productImageDeatails.save()

def listProduct(params):
    """
    Gets all details of all the products in the database
    
    :return ProductList: All the products
    """
    ProductList = models.Product.objects
    if 'id' in params:
        ProductList = ProductList.get(id=params['id'])
    if len(params) == 0:
        ProductList = ProductList.all().order_by('id')
    return ProductList

def getProduct(productObj):
    """
    Gets all details of a products in the database
    
    :return product: the product details
    """
        
    product = models.Product.objects.get(pk=productObj.id)
    return product

def getProductImages(productObj):
    """
    Gets details of all the images of a products in the database
    
    :return product_image: the image details
    """
    product_images = models.ImageMapping.objects.filter(product=productObj.id)
    return product_images

def deleteProducts(deleteObj):

    """
    delete the  product from the database
    :type deleteObj: object 
    :param deleteObj: An instance with the following attributes 
                       productId
                      
    
  
    """
    #deleting product door object
    
    try:
        product_door = ProductDoors.objects.filter(product=deleteObj.id)
        product_door.delete()
    except:
        pass
    #deleting product tax
    
    try:
        product_tax = TaxMapping.objects.filter(product=deleteObj.id)
        product_tax.delete()
    except:
        pass
    #deleting product hinges object
    
    try:
        product_hinges = ProductHinges.objects.filter(product=deleteObj.id)
        product_hinges.delete()
    except:
        pass
     #deleting the image mapping
   
    try:
        product_images = ImageMapping.objects.get(pk=deleteObj.id)
        product_images.delete()
    except:
        pass
    #deleting the product
    
    try:
        product = models.Product.objects.get(pk=deleteObj.id)
        product.delete()
    except:
        pass
   
def deleteProductImages(deleteObj):
    
    """
    delete all mapping images
    """
    product_images = models.ImageMapping.objects.get(id=deleteObj.image_id)
    product_images.delete()
    

def editProduct(productObj):
    
    """
    function is used to create a product
    """
    try:
        product_image=productObj.image.name
    except:
        product_image = None
    #tax = Tax.objects.get(id=productObj.tax)
    category = models.Category.objects.get(id=productObj.category)
    if not productObj.sub_category:
        sub_category=None
    else:
        sub_category = models.SubCategory.objects.get(id=productObj.sub_category)
    #tax = 
    
    productDeatails = models.Product.objects.get(id=productObj.id)
    productDeatails.category=category
    productDeatails.sub_category=sub_category
    productDeatails.product_name=productObj.product_name
   # productDeatails.product_code=productObj.product_code
    productDeatails.short_description=productObj.short_description
    productDeatails.descriptions=productObj.descriptions
    productDeatails.product_price=productObj.product_price
    #productDeatails.tax=tax
    productDeatails.min_height=productObj.min_height
    productDeatails.max_height=productObj.max_height
    productDeatails.height_scale=productObj.height_scale
    productDeatails.min_width=productObj.min_width
    productDeatails.max_width=productObj.max_width
    productDeatails.width_scale=productObj.width_scale
    productDeatails.min_depth=productObj.min_depth
    productDeatails.max_depth=productObj.max_depth
    productDeatails.depth_scale=productObj.depth_scale
    productDeatails.is_hinges=productObj.hinges
    productDeatails.image=product_image
    productDeatails.is_door=productObj.door
    productDeatails.cabinet=productObj.cabinet
    productDeatails.is_drawer=productObj.drawers
    productDeatails.video_url = productObj.video_url   
    productDeatails.discount = productObj.discount        
    productDeatails.is_custom = productObj.is_custom
    productDeatails.save()
    product_id = productDeatails.id
    
    return product_id







def listProductImages(params):
    """
    Gets all details of all the product images in the database
    
    :return imageList: All the product images
    """
    
    imageList = models.ImageMapping.objects
    if len(params) == 0:
        imageList = imageList.all().order_by('id')  
    return imageList


 
    