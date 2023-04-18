from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

        widgets = {
            'first_name':forms.TextInput(attrs={"class":"form-control", "placeholder":"First Name"}),
            'last_name':forms.TextInput(attrs={"class":"form-control", "placeholder":"Last Name"}),
            'email':forms.TextInput(attrs={"class":"form-control", "placeholder":"Email"}),
            'address':forms.TextInput(attrs={"class":"form-control", "placeholder":"Address"}),
            'postal_code':forms.TextInput(attrs={"class":"form-control", "placeholder":"Postal Code"}),
            'city':forms.TextInput(attrs={"class":"form-control", "placeholder":"City"})
        }
