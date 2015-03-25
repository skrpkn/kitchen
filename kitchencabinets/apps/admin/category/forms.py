from django import forms




class CategoryForm(forms.Form):
    id  = forms.CharField(required=False)
    category_name = forms.CharField(required='True',max_length=100,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Category name'}))
    #category_image = forms.CharField(required='False',max_length=100,label= "Category Image",widget=forms.ValidationTextInput(attrs={'regExp':'[a-zA-Z\s]+'}))
    
    
    category_image=forms.FileField(required=False,label= "Icon")
    category_status = forms.CharField(label= "Status")
                      
   
