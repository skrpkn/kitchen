from django import forms
#from apps.users.registration.models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
import re

# Create your models here.

class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100, required = False)
    last_name = forms.CharField(max_length=100, required = False)
    email = forms.EmailField(max_length=100, required = True)
     
                        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            return None
        return email

class AuthenticationForm(AuthenticationForm):
        username = forms.EmailField(label="E-mail")
        
class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        if 'newpassword1' in cleaned_data and 'newpassword2' in cleaned_data:
            if cleaned_data.get('newpassword1') != cleaned_data.get('newpassword2'):
                raise forms.ValidationError(("The two password fields didn't match."))
        
        if len(cleaned_data.get('newpassword1')) < 8:
            raise forms.ValidationError(("Your password has to be at least 8 characters long"))
        
        if not re.search('\d+', cleaned_data.get('newpassword1')) or not re.search('([a-zA-Z])+', cleaned_data.get('new  password1')):
            raise forms.ValidationError(("Your password needs to contain at least one number and one character"))
        
        return cleaned_data

# class ForgotPasswordForm(forms.Form):
#     email = forms.EmailField(max_length=100)
#     
# class forgotPasswordRedirectForm(forms.Form):
#     new_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
#     confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)
