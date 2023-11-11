from django import forms 

class SignUp(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"Your Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}))
    repassword = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Repeat Your Password"}))

    def clean(self):
        cleaned_data = super().clean()

        Valname = self.cleaned_data["name"]
        Valpassword = self.cleaned_data["password"]
        Valrepassword = self.cleaned_data["repassword"]

        if(Valpassword != Valrepassword):
            print("Yes password")
            raise forms.ValidationError("Password and Repassword should be same")

        if(not Valname[0].isalpha()):
            print("No password")
            raise forms.ValidationError("Name should start with alphabets ")

        if(len(Valpassword) < 10 and len(Valrepassword) < 10):
            print("No yes password")
            raise forms.ValidationError("Length of password should be greater then 10.")

        return cleaned_data


class SignIn(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Your Name"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Your Password"}))

    def clean_name(self):
        name = self.cleaned_data["name"]

        if(not name[0].isalpha()):
            # print("No password") 
            raise forms.ValidationError("Name should start with alphabets ")

        return name

