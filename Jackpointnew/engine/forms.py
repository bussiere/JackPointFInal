from django import forms

class LoginForm(forms.Form):
    Username = forms.CharField(max_length=100)
    PW = forms.CharField( widget=forms.PasswordInput, label="Your Password" )