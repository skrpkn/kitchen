from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('apps.users.registration.views',
                      
                       
                       
)

from django.conf.urls import *


urlpatterns += patterns('apps.users.registration.views',
   url(r'forgot-password/', 'forgot_password', name="forgot-password"
   ),
)