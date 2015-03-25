from django import template
from constants import Collection
from apps.admin.cabinet import cabinetBll
import locale
register = template.Library()

# price calculation
# price object => priceObj.width, priceObj.height and priceObj.depth
def priceCalculation(product, priceObj= Collection()):
    # material price
    price = product.material.price
    cabinetData = cabinetBll.getProductCabinet(product)
    # total cabinets size
    width = height = depth = 0
    # get custom width or default (minimum width) 
    if hasattr(priceObj, 'width'):
        width = priceObj.width
    else:  
        width = product.min_width    
    # get custom height or default (minimum height) 
    if hasattr(priceObj, 'height'):
        height = priceObj.height
    else:  
        height = product.min_height     
    # get custom depth or default (minimum depth)    
    if hasattr(priceObj, 'depth'):
        depth = priceObj.depth
    else:  
        depth = product.min_depth 
     
    #convert to centimetre  devide by 1000       
    widthMtr = width / 1000
    heightMtr = height / 1000
    depthMtr = depth / 1000
    total = []
    # append cabinet price
    if len(cabinetData) > 0:
        for single in cabinetData:
            #tsqm = single.size+ tsqm
            subTotal = single.size* price
            if(single.cabinet_construction.width == 1):
                subTotal = subTotal * widthMtr # multiply with width
            if(single.cabinet_construction.height == 1):
                subTotal = subTotal * heightMtr # multiply with height
            if(single.cabinet_construction.depth == 1):
                subTotal = subTotal * depthMtr # multiply with depth
            total.append(subTotal)
            
    # if no cabinets attached, then return material price      
    if len(total) == 0:
        total = [price]    
    # array sum  => sum(array)     
    price = sum(total)    
#       TSQM x DM =
    #locale.setlocale( locale.LC_ALL, '' )
    #price = locale.currency(price, grouping=True )  
    return price
    
    
def ranges(product):
    priceObj = Collection()
    resultDict = {}
# width scale manipulations     
    width_minimum = product.min_width or 0
    width_maximum = product.max_width or 0
    width_scale = product.width_scale or 0
    
    height_minimum = product.min_height or 0
    height_maximum = product.max_height or 0
    height_scale = product.height_scale or 0
    
    depth_minimum = product.min_depth or 0
    depth_maximum = product.max_depth or 0
    depth_scale = product.depth_scale or 0
    
    #price 
    priceObj.width = width_minimum
    priceObj.height = height_minimum
    priceObj.depth = depth_minimum
    priceObj.price = product.product_price
    price = priceCalculation(product, priceObj)
    minPrice = price
    resultDict[0] = {'width':width_minimum, 'height':height_minimum, 'depth':depth_minimum,'price':price}
    count = 1
#     check width scale
    if(width_scale and width_minimum != width_maximum):
#         loop up to maximum
        while width_minimum < width_maximum:
            width_minimum = width_minimum + width_scale
#             confirm minimum less than maximum
            if width_minimum <= width_maximum:
                #price 
                priceObj.width = width_minimum
                priceObj.height = height_minimum
                priceObj.depth = depth_minimum
                price = priceCalculation(product, priceObj)
                resultDict[count] = {'width':width_minimum, 'height':height_minimum, 'depth':depth_minimum,'price':price}
                count = count + 1
                
    if width_minimum != width_maximum:
        #price 
        priceObj.width = width_maximum
        priceObj.height = height_maximum
        priceObj.depth = depth_maximum
        price = priceCalculation(product, priceObj)
        resultDict[count] = {'width':width_maximum, 'height':height_maximum, 'depth':depth_maximum,'price':price}
        
    #     check height scale
    if(height_scale and height_minimum != height_maximum):
        width_minimum = product.min_width or 0
        width_maximum = product.max_width or 0
#         loop up to maximum
        while height_minimum < height_maximum:
            height_minimum = height_minimum + height_scale
#             confirm minimum less than maximum
            if height_minimum <= height_maximum:
                
                #price 
                priceObj.width = width_minimum
                priceObj.height = height_minimum
                priceObj.depth = depth_minimum
                price = priceCalculation(product, priceObj)
                resultDict[count] = {'width':width_minimum, 'height':height_minimum, 'depth':depth_minimum,'price':price}
                count = count + 1
                
    if height_minimum != height_maximum:
        #price 
        priceObj.width = width_maximum
        priceObj.height = height_maximum
        priceObj.depth = depth_maximum
        price = priceCalculation(product, priceObj)
        resultDict[count] = {'width':width_maximum, 'height':height_maximum, 'depth':depth_maximum,'price':price}
    
    #     check height scale
    if(depth_scale and depth_minimum != depth_maximum):
        height_minimum = product.min_height or 0
        height_maximum = product.max_height or 0     
#         loop up to maximum
        while depth_minimum < depth_maximum:
            depth_minimum = depth_minimum + depth_scale
#             confirm minimum less than maximum
            if depth_minimum <= depth_maximum:
                
                #price 
                priceObj.width = width_minimum
                priceObj.height = height_minimum
                priceObj.depth = depth_minimum
                price = priceCalculation(product, priceObj)
                resultDict[count] = {'width':width_minimum, 'height':height_minimum, 'depth':depth_minimum,'price':price}
                count = count + 1
                
    if depth_minimum != depth_maximum:
        #price 
        priceObj.width = width_maximum
        priceObj.height = height_maximum
        priceObj.depth = depth_maximum
        price = priceCalculation(product, priceObj)
        resultDict[count] = {'width':width_maximum, 'height':height_maximum, 'depth':depth_maximum,'price':price}
# initialise         
    count = 1    
    product_id = product.id
    #resultDict['id'] = product.id
    
    return { "result":  resultDict,"name":product.product_name,"id":product.id}

register.inclusion_tag('range_list.html')(ranges)