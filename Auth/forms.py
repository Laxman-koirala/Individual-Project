from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
class SignupForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password(again)',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Guess Strong Password',
    widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields = ['username','first_name','last_name','email']
        labels = {'email': 'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.TextInput(attrs={'class':'form-control '}),
        'username':forms.TextInput(attrs={'class':'form-control'})}
