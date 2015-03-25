from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.users.product.views',
    #url(r'^list/$', 'listProducts'),
    url(r'^add-to-cart/(?P<price>[^/]+)/(?P<product_id>\w+)/$', 'addtocart', {} ,name="addtocart"),
    #url(r'^shoppingcart/$', 'shoppingcart', {} ,name="shoppingcart"),
    url(r'^mycart/$', 'add_cart_to_session'),
    url(r'^remove-from-cart/$', 'deleteCartProduct'),
    #url(r'^delete/(?P<productId>\w+)/$', 'deleteCartProduct'),
    #url(r'^delete/$', 'deleteCartProduct'),
    
)