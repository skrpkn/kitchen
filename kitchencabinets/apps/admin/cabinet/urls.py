from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.cabinet.views',
    url(r'^list/$', 'listCabinet'),
    url(r'^create/$', 'createCabinet'),
    url(r'^edit/(?P<cabinetId>\d+)/$', 'editCabinet'),
    url(r'^delete/(?P<cabinetId>\d+)/$', 'deleteCabinet'),
    
)