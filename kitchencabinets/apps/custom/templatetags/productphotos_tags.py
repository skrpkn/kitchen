from django import template
from apps.admin.product import productBll
register = template.Library()
def productphotos(product):
    product_image_list = productBll.getProductImages(product)
    return { "product_image_list":  product_image_list}

register.inclusion_tag('productphotos.html')(productphotos)