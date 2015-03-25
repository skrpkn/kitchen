from django import template
from constants import Collection




register = template.Library()



def cart(request):
    items_length = 0
    try:
        session_items = request.session['cart']
        for val in session_items:
            quantity = val.quantity
            items_length = items_length + int(quantity)
    except:
        items_lenght = 0
    return { "items_length":  items_length}

register.inclusion_tag('cart.html')(cart)