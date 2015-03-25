from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.drawers.views',
    url(r'^list/$', 'listDrawers'),
    url(r'^create/$', 'createDrawers'),
    url(r'^edit/(?P<drawersId>\d+)/$', 'editDrawers'),
    url(r'^delete/(?P<drawersId>\d+)/$', 'deleteDrawers'),
    
)