from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms
from .models import GENDER


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter your email address"}),
        required=True,
        help_text='Required. Inform a valid email address.',
    )
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "First Name", "class": "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Last Name", "class": "form-control"}))
    gender = forms.ChoiceField(
        choices=GENDER, widget=forms.Select(attrs={"class": "form-control"}))
    is_seller = forms.BooleanField(widget=forms.CheckboxInput(
    ), label="Check this box if you want to register as a seller", required=False)

    class Meta:
        model = CustomUser
        fields = ("email", "first_name", "last_name", "is_seller", "gender")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'gender', 'is_seller')
        first_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'First Name', 'class': 'form-control'}), required=True)
        last_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Last Name', 'class': 'form-control'}), required=True)
        gender = forms.ChoiceField(
        choices=GENDER, widget=forms.Select(attrs={"class": "form-control"}))
        is_seller = forms.BooleanField(widget=forms.CheckboxInput(), label="Check this box if you want to register as a seller", required=False)


class ProfileFirstUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'gender', 'is_seller')
        first_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'First Name', 'class': 'form-control'}), required=True)
        last_name = forms.CharField(widget=forms.TextInput(
            attrs={'placeholder': 'Last Name', 'class': 'form-control'}), required=True)
        gender = forms.ChoiceField(
        choices=GENDER, widget=forms.Select(attrs={"class": "form-control"}))
    is_seller = forms.BooleanField(widget=forms.CheckboxInput(
    ), label="Check this box if you want to register as a seller", required=False)