from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.subCategory.views',
    
    url(r'^list/$', 'listSubCategory'),
    url(r'^create/$', 'createSubCategory'),
    url(r'^edit/(?P<subCategoryId>\d+)/$', 'editSubCategory'),
    url(r'^delete/(?P<subCategoryId>\d+)/$', 'deleteSubCategory'),
    
    url(r'^filter/(?P<cat_id>\d+)/$', 'filterSubCategory'),
 #   url(r'^filter/$', 'filterSubCategory'),
    
    
)