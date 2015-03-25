from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.views import login,logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from apps.admin.initial.views import index
admin.autodiscover()

urlpatterns = patterns('',
   
    url(r'^login/$', login),
    url(r'^logout/$', logout),
   
)
