from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import  HttpResponseRedirect
from constants import ADMIN
from django.contrib.auth.views import login
# from constants import Collection
# import usersBll



                                                                             
def index(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return render_to_response('home/index.html',context_instance=RequestContext(request))
        else:
            return render_to_response('home/user_index.html',context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('login')
        


