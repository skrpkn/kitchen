from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login,logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.admin.initial.views import index
from apps.users.registration.views import sign_up, resetPassword, forgot_password
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from apps.users.registration.registrationBll import forgotPassword
from django.contrib.auth import models
from apps.users.product.views import listProducts, shoppingcart
    
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/$', login ),
    url(r'^logout/$', logout),
    
    url(r'^admin/category/', include('apps.admin.category.urls')),
    url(r'^admin/subcategory/', include('apps.admin.subCategory.urls')),
    url(r'^admin/hinges/', include('apps.admin.hinges.urls')),
	url(r'^admin/door/', include('apps.admin.door.urls')),
    url(r'^admin/cabinet/', include('apps.admin.cabinet.urls')),
    url(r'^admin/product/', include('apps.admin.product.urls')),
    url(r'^admin/drawers/', include('apps.admin.drawers.urls')),
    url(r'^admin/tax/', include('apps.admin.tax.urls')),
    url(r'^admin/materials/', include('apps.admin.materials.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
     #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('apps.users.registration.urls', namespace="accounts")),

    url(r'^signup/$', sign_up),    
    url(r'^resetpassword/$', resetPassword),   
#     url(r'^forgotpassword/$', forgot_password),  
#     url(r'^confirmpassword/(?P<mail>[-A-Za-z0-9%]+)/$', forgotPasswordConfirm),  
   # url(r'^ResetPassword/$', ),    
    #url(r'^users/', include('apps.users.registration.urls')),
    url(r'^product/', include('apps.users.product.urls')),
    url(r'^list/$', listProducts),
    url(r'^shoppingcart/$', shoppingcart, {} ,name="shoppingcart"),
    
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
     #url(r'^admin/', include(admin.site.urls)),
