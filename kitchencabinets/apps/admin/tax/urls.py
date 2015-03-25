from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.tax.views',
    url(r'^list/$', 'listTax'),
    url(r'^create/$', 'createTax'),
    url(r'^edit/(?P<taxId>\d+)/$', 'editTax'),
    url(r'^delete/(?P<taxId>\d+)/$', 'deleteTax'),
  
    
    
    
)