from django import forms




class DoorForm(forms.Form):
    id  = forms.CharField(required=False)
    door_name = forms.CharField(required='True',max_length=100,label= "Name", widget=forms.TextInput(attrs={'placeholder': 'Door name'}))
    door_price = forms.FloatField(required=False,label= "Price/ Square metre ",widget=forms.TextInput(attrs={'placeholder': 'Price'}))
    description = forms.CharField(required=False,max_length=1000,label= "Description", widget=forms.Textarea(attrs={'placeholder': 'Door description'}))
    estimated_time = forms.IntegerField(required=False,label= "Estimated Time(in days)",widget=forms.TextInput(attrs={'placeholder': 'Estimated Time'}))
                      

class ProductDoorForm(forms.Form):
    id  = forms.CharField(required=False)
    product = forms.CharField(required=False,label="Product")
    door = forms.CharField(required=False,label="Door")
    pieces_count = forms.IntegerField(required=False, label="Pieces Count")
