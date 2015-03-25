from django import forms
from django.forms import extras




class TaxForm(forms.Form):
    id  = forms.CharField(required=False)
    tax_name = forms.CharField(required='True',max_length=100,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Tax name'}))
    tax_date = forms.DateField(required=False,label="Last Modified Date",widget=extras.SelectDateWidget)
    tax_status = forms.CharField(label= "Status")
    tax_rate = forms.FloatField(required=False,label= "Tax Rate",widget=forms.TextInput(
                                            attrs={'placeholder': 'Tax rate'}))
    
        
    
              
