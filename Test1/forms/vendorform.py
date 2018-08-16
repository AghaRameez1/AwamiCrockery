from django.forms import ModelForm

from Test1.models import vendorModel
from Test1.validator import ascii_validator, numeric_validator


class vendorForm(ModelForm):
    class Meta:
        model = vendorModel
        fields = ['first_name', 'last_name', 'price', 'item_code']

    def __init__(self,*args,**kwargs):
        super(vendorForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].required= True
        self.fields['first_name'].widget.attrs['placeholder']="First Name"
        self.fields['first_name'].widget.attrs['class']="form-control"
        self.fields['first_name'].widget.attrs['style']="height: 29px"

        self.fields['last_name'].required= True
        self.fields['last_name'].widget.attrs['placeholder']="Last Name"
        self.fields['last_name'].widget.attrs['class']="form-control"
        self.fields['last_name'].widget.attrs['style'] = "height: 29px"

        self.fields['price'].required= True
        self.fields['price'].widget.attrs['placeholder'] = "Price In Rupees"
        self.fields['price'].widget.attrs['class'] = "form-control"

        self.fields['item_code'].required= True
        self.fields['item_code'].widget.attrs['placeholder']="Item Code"
        # self.fields['item_code'].widget.attrs['class']="form-control"

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        ascii_validator(first_name)
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        ascii_validator(last_name)
        return last_name

    def clean_price(self):
        price = self.cleaned_data['price']
        numeric_validator(price)
        return price
