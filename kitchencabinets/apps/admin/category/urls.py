from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.category.views',
    url(r'^list/$', 'listCategory'),
    url(r'^create/$', 'createCategory'),
    url(r'^edit/(?P<categoryId>\d+)/$', 'editCategory'),
    url(r'^reorder/$', 'reorderCategory'),
 #   url(r'^editCategory/(?P<categoryId>\d+)/$', 'editCategory'),
 #   url(r'^editCategory/$', 'editCategory'),
    url(r'^delete/(?P<categoryId>\d+)/$', 'deleteCategory'),
    
 
    
    
    
)