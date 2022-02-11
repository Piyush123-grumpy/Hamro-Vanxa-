from django.contrib.auth.forms import UserCreationForm

from phonenumber_field.phonenumber import PhoneNumber

from account.models import Account
from django import forms

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control my-2','placeholder':'Enter Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm Password'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Phone Number'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter City'}))
    class Meta:
        model = Account
        fields = ['first_name','last_name','username','email','password1','password2','phone_number','state','city']