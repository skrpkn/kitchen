from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
import forms
from constants import Collection, REG_PASSWORD_SUBJECT,\
    REG_PASSWORD_BODY_USERNAME, REG_PASSWORD_BODY_PASS, EMAIL_VALIDATION,\
    FORGET_PASSWORD, FORGOT_PASSWORD_URL
import registrationBll
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.views import password_reset, password_reset_done
from django.shortcuts import render



# def sign_up(request):
#     """ User sign up form """
#     if request.method == 'POST':
#         data = request.POST.copy() # so we can manipulate data
# 
#         # random username
#         data['username'] = ''.join([choice(letters) for i in xrange(30)])
#         form = SignUpForm(data)
#             
#         if form.is_valid():
#             user = form.save()
#             return HttpResponseRedirect('/sign_up_success.html')
#     else:
#         form = SignUpForm()
# 
#     return render_to_response('registration/sign_up.html', {'form':form},
#                               context_instance=RequestContext(request))


def sign_up(request):
    """
    for registartion
    """
    
    usersObj = Collection()
    form = forms.UserRegistrationForm()
    data = {'form': form}
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            if not form.clean_email():
                messages.error(request, 'Already this Email address have an associated account', extra_tags='email')    
                return render_to_response('registration/sign_up.html', data, context_instance=RequestContext(request))
            usersObj.first_name=request.POST['first_name']
            usersObj.last_name=request.POST['last_name']
            usersObj.email = usersObj.username = request.POST['email']
            usersObj.subject = REG_PASSWORD_SUBJECT
            usersObj.password = registrationBll.createUser(usersObj)
            usersObj.msg =  REG_PASSWORD_BODY_USERNAME +usersObj.username + REG_PASSWORD_BODY_PASS + usersObj.password
            registrationBll.sendMail(usersObj)
            print usersObj.username
            user = authenticate(username=usersObj.username, password=usersObj.password)
            login(request, user)
             
             
    return render_to_response('registration/sign_up.html', data, context_instance=RequestContext(request))
           

@login_required
def resetPassword(request):
    """
    Reset the password for the logined user
    """
    data = {}
    usersObj = Collection()
    form = forms.ResetPasswordForm()
    if request.method == 'POST':
        form = forms.ResetPasswordForm(request.POST)
        if form.is_valid():
            usersObj.currentUser = request.user
            usersObj.old_password=request.POST['old_password']
#             if not request.user.check_password(usersObj.old_password):
            usersObj.new_password=request.POST['new_password']
            usersObj.confirm_password=request.POST['confirm_password']
            if usersObj.new_password == usersObj.confirm_password:
                registrationBll.resetPassword(usersObj)
#             else:
                
            return HttpResponseRedirect('/')

    data = {'form': form}
    return render_to_response('registration/resetPassword.html', data, context_instance=RequestContext(request))
        
# def forgotPassword(request):
#     """
#     function to give back the forgotten password
#     """     
#     usersObj = Collection()
#     form = forms.ForgotPasswordForm()
#     if request.method == 'POST':
#         form = forms.ForgotPasswordForm(request.POST)
#         if form.is_valid():
#             usersObj.email=request.POST['email']
#             try:
#                 registrationBll.checkEmailValidation(usersObj)
#             except:
#                 messages.success(request, EMAIL_VALIDATION)
#             usersObj.subject = FORGET_PASSWORD
#             encrypted_code = registrationBll.encrypt(usersObj)
#             print type(encrypted_code)
#             usersObj.msg = '/n/n click the link for reset your password\n'+FORGOT_PASSWORD_URL+encrypted_code+'/\n\n'
#             registrationBll.sendMail(usersObj)
# #             username = registrationBll.getUserName(usersObj.email)
# #             password = registrationBll.forgotPassword(usersObj.email)
# #             registrationBll.sendMail(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, usersObj.email, password, username)
# 
# 
#     data = {'form': form}
#     return render_to_response('users/registration/forgotPassword.html', data, context_instance=RequestContext(request))
# 
# def forgotPasswordConfirm(request, mail):
#     """
#     function to change password for forgotpassword option
#     """
#     print "forget password"
# #     usersObj = Collection()
# #     registrationBll.decrypt()
# #     form = forms.forgotPasswordRedirectForm()
# #     if request.method == 'POST':
# #         form = forms.forgotPasswordRedirectForm(request.POST)
# #         if form.is_valid():
# #     return HttpResponse(mail+" "+ str(request)
#     print "ah ah ah   "+mail


def forgot_password(request):
    if request.method == 'POST':
        return password_reset(request, 
            from_email=request.POST.get('email'))
    else:
        return render(request, 'registration/forgot_password.html')




