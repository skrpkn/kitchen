from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.hinges.views',
    url(r'^list/$', 'listHinges'),
    url(r'^create/$', 'createHinges'),
    url(r'^edit/(?P<hingesId>\d+)/$', 'editHinges'),
    url(r'^delete/(?P<hingesId>\d+)/$', 'deleteHinges'),
    
)