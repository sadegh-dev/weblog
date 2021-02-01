from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your username'}))
    password = forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'your password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'your username'}))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'your email'}))
    password = forms.CharField(label='password', max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'your password'}))
    password2 = forms.CharField(label='confirm password', max_length=30, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'your password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user.exists():
            raise forms.ValidationError('this email already exists')
        return email
    
    # Way 1 : password
    """
    def clean_password2(self):
        p = self.cleaned_data['password']
        p2 = self.cleaned_data['password2']
        if p != p2 :
            raise forms.ValidationError('passwords must match')
        return p
    """

    # Way 2 : password
    def clean(self):
        cleaned_data = super().clean()
        p = cleaned_data.get('password')
        p2 = cleaned_data.get('password2')
        if p and p2 :
            if p != p2 :
                raise forms.ValidationError('passwords must match')

        



