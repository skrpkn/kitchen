from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.product.views',
    url(r'^list/$', 'listProducts'),
    url(r'^create/$', 'createProduct'),
    url(r'^view/(?P<productId>\d+)/$', 'viewProducts'),
    url(r'^edit/(?P<productId>\d+)/$', 'editProduct'),
    url(r'^delete/(?P<productId>\d+)/$', 'deleteProduct'),
    url(r'^deleteImage/$', 'deleteProductImages'),
    
)