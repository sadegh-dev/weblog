from django import forms

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'your password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'your password'}))
    