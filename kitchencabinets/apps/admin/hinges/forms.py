from django import forms




class HingesForm(forms.Form):
    id  = forms.CharField(required=False)
    hinges_name = forms.CharField(required=False,max_length=200,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Hinges name'}))
    
    hinges_unit_price = forms.CharField(required=False,label= "Unit Price", widget=forms.TextInput(attrs={'placeholder': 'Hinges unit price'}))
                      
   

class ProductHinges(forms.Form):
    id  = forms.CharField(required=False)
    product = forms.CharField(required=False,label="Product")
    hinges = forms.CharField(required=False,label="Hinges")
    hinges_min = forms.IntegerField(required=False,label="Minimum Hinges", widget=forms.TextInput(attrs={'placeholder': 'Minimum hinges'}))
    hinges_max = forms.IntegerField(required=False,label="Maximum Hinges",widget=forms.TextInput(attrs={'placeholder': 'Maximum hinges'}))
    