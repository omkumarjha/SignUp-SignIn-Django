from django import forms 

class SignUp(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Your Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repeat Your Password"}))


class SignIn(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}))
