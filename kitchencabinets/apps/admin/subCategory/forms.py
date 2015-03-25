from django import forms
import subCategoryBll
from django.contrib.admin.widgets import FilteredSelectMultiple


   



class SubCategoryForm(forms.Form):
    id  = forms.CharField(required=False)
    category = forms.CharField(required='True',label="Category")
    sub_category_name = forms.CharField(required='True',max_length=100,label= "Subcategory", widget=forms.TextInput(attrs={'placeholder': 'Subcategory name'}))
    
    #sub_category_image=forms.FileField(required=False,label= "Icon")
    sub_category_status = forms.CharField(label= "Status")
                      

