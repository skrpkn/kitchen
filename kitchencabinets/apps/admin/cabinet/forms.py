from django import forms




class CabinetForm(forms.Form):
    id  = forms.CharField(required=False)
    cabinet_name = forms.CharField(required=False,max_length=200,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Cabinet name'}))
    
                      
   

class ProductCabinet(forms.Form):
    id = forms.CharField(required=False)
    product = forms.CharField(required=False,label="Product")
    cabinet = forms.CharField(required=False,label="Cabinet")
    size = forms.FloatField(required=False,label= "Size",widget=forms.TextInput(attrs={'placeholder': 'Cabinet size'}))

