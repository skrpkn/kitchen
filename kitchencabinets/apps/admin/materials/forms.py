from django import forms




class MaterialForm(forms.Form):
    id  = forms.CharField(required=False)
    materials_name = forms.CharField(required=False,max_length=200,label= "Material Name", widget=forms.TextInput(attrs={'placeholder': 'Material name'}))
    descriptions = forms.CharField(required=False,max_length=1000,label= "Material Description", widget=forms.Textarea(attrs={'placeholder': 'Material description'}))
    materials_price = forms.FloatField(required=False,label= "Price/Square Metre ")
    status = forms.CharField(label= "Status")
    
