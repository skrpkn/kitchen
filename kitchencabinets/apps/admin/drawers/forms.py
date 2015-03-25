from django import forms




class DrawersForm(forms.Form):
    id  = forms.CharField(required=False)
    drawer_name = forms.CharField(required='True',max_length=200,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Drawers name'}))
    
    drawer_unit_price = forms.CharField(required='True',label= "Unit Price", widget=forms.TextInput(attrs={'placeholder': 'Drawer unit price'}))
                      
   

class ProductDrawersForm(forms.Form):
    id  = forms.CharField(required=False)
    product = forms.CharField(required=False,label="Product")
    drawer = forms.CharField(required=False,label="Drawer")
    product_drawers_quantity = forms.IntegerField(required=False,label= "Quantity", widget=forms.TextInput(attrs={'placeholder': 'Drawer Quantity'}))
    product_drawer_total_price = forms.FloatField(required=False,label= "Total Price", widget=forms.TextInput(attrs={'placeholder': 'Drawer Total Price'}))
