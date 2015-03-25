from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.admin.door.views',
    url(r'^list/$', 'listDoors'),
    url(r'^create/$', 'createDoor'),
    url(r'^edit/(?P<doorId>\d+)/$', 'editDoor'),
    url(r'^delete/(?P<doorId>\d+)/$', 'deleteDoor'),
)