from django import forms 

class SignUp(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}),error_messages={"required":"Enter your name "})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Your Email"}),error_messages={"required":"Enter your email "})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}),error_messages={"required":"Enter your password "})
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repeat Your Password"}),error_messages={"required":"Enter your repassword "})

    def clean(self):
        cleaned_data = super().clean()

        name = cleaned_data.get("name") # why we used this not self.cleaned_data["name"] Reason is : Agar koi value nhi di gayi hogi to yeh none return kardega .
        password = cleaned_data.get("password")
        email = cleaned_data.get("email")
        repassword = cleaned_data.get("repassword")

        if(password and repassword and password != repassword):
            raise forms.ValidationError("Password and Repassword should be same")

        if(name and not name[0].isalpha()): # Agar name exist kar raha hai then hum condition dekhenge 
            raise forms.ValidationError("Name should start with alphabets ")

        if(password and repassword and len(password) < 10 and len(repassword) < 10):
            raise forms.ValidationError("Length of password should be greater then 10.")


class SignIn(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}),error_messages={"required":"Enter your name "})
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}),error_messages={"required":"Enter your password "})

    def clean_name(self):
        name = self.cleaned_data["name"]

        if(not name[0].isalpha()):
            raise forms.ValidationError("Name should start with alphabets ")

        return name

