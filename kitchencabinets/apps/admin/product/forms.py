from django import forms


CHOICES = (('1', 'Yes',), ('2', 'No',))

class ProductForm(forms.Form):
    id  = forms.CharField(required=False)
    materials = forms.CharField(required=True,label="Material")
    cabinet = forms.CharField(required=True,label="Cabinet Type")
    category = forms.CharField(required=True,label="Category")
    sub_category = forms.CharField(required=False,label="Subcategory")
    product_name = forms.CharField(required='True',max_length=100,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Product name'}))
    product_code = forms.CharField(required='True',max_length=100,label= "Code", widget=forms.TextInput(attrs={'placeholder': 'Product code'}))
    short_description = forms.CharField(required=False,max_length=100,label= "Short Description", widget=forms.Textarea(attrs={'placeholder': 'Product short description'}))
    descriptions = forms.CharField(required=False,max_length=1000,label= "Description", widget=forms.Textarea(attrs={'placeholder': 'Product description'}))
    product_price = forms.FloatField(required='True',label= "Price",widget=forms.TextInput(attrs={'placeholder': 'Product price'}))
    tax = forms.CharField(required=False,label="Tax")
    min_height = forms.FloatField(required=False,label= "Minimum Height",widget=forms.TextInput(attrs={'placeholder': 'Product minimum height'}))
    max_height = forms.FloatField(required=False,label= "Maximum Height",widget=forms.TextInput(attrs={'placeholder': 'Product maximum height'}))
    height_scale = forms.FloatField(required=False,label= "Height Scale",widget=forms.TextInput(attrs={'placeholder': 'Product height scale'}))
    min_width = forms.FloatField(required=False,label= "Minimum Width",widget=forms.TextInput(attrs={'placeholder': 'Product minimum width'}))
    max_width = forms.FloatField(required=False,label= "Maximum Width",widget=forms.TextInput(attrs={'placeholder': 'Product maximum width'}))
    width_scale = forms.FloatField(required=False,label= "Width Scale",widget=forms.TextInput(attrs={'placeholder': 'Product width scale'}))
    min_depth = forms.FloatField(required=False,label= "Minimum Depth",widget=forms.TextInput(attrs={'placeholder': 'Product minimum depth'}))
    max_depth = forms.FloatField(required=False,label= "Maximum Depth",widget=forms.TextInput(attrs={'placeholder': 'Product maximum depth'}))
    depth_scale = forms.FloatField(required=False,label= "Depth Scale",widget=forms.TextInput(attrs={'placeholder': 'Product depth scale'}))
    discount = forms.FloatField(required=False,label= "Total Price Discount (in %)",widget=forms.TextInput(attrs={'placeholder': 'Total price discount'}))
    is_hinges = forms.ChoiceField(required=False,label= "Is Hinge", widget=forms.RadioSelect,choices=CHOICES)
    is_door = forms.ChoiceField(required=False,label= "Is Door",  widget=forms.RadioSelect,choices=CHOICES)
    is_cabinet = forms.ChoiceField(required=False,label= "Is Cabinet", widget=forms.RadioSelect,choices=CHOICES)
    is_drawer = forms.ChoiceField(required=False,label= "Is Drawer", widget=forms.RadioSelect,choices=CHOICES)
    image=forms.FileField(required=False,label= "Product Icon")
    video = forms.CharField(max_length=200,label= "Video Url", widget=forms.TextInput(attrs={'placeholder': 'Video url'}))
    is_custom = forms.ChoiceField(required=False,label= "Custom Size available for this product?",  widget=forms.RadioSelect,choices=CHOICES) 
         

