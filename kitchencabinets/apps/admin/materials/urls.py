from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.materials.views',
    url(r'^create/$', 'createMaterial'),
     url(r'^list/$', 'listMaterial'),
     url(r'^edit/(?P<materialId>\d+)/$', 'editMaterial'),
    url(r'^delete/(?P<materialId>\d+)/$', 'deleteMaterials'),
)