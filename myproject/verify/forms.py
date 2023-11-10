from django import forms 

class SignUp(forms.Form):
    name = forms.CharField(label="",widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(label="",widget=forms.TextInput(attrs={"placeholder":"Your Email"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}))
    repassword = forms.CharField(label="",widget=forms.PasswordInput(attrs={"placeholder":"Repeat Your Password"}))