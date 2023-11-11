from django.shortcuts import render
from .forms import SignUp , SignIn

# Create your views here.

def home(request):
    return render(request,'verify/home.html')

def signup(request):
    if request.method == "POST":
        fm = SignUp(request.POST)

        if fm.is_valid():
            print("Form is validated successfully ")
            print("Name : ",fm.cleaned_data["name"])
            print("email : ",fm.cleaned_data["email"])
            print("password : ",fm.cleaned_data["password"])
            print("repassword : ",fm.cleaned_data["repassword"])
            fm = SignUp()
        else:
            print("Error is comming....")

    else:
        fm = SignUp()
    return render(request,'verify/signup.html',{"forms":fm})
    
def signin(request):
    if request.method == "POST":
        fm = SignIn(request.POST)

        if fm.is_valid():
            print("Form is validated successfully ")
            print("Name : ",fm.cleaned_data["name"])
            print("password : ",fm.cleaned_data["password"])
            fm = SignIn()
        else:
            print("Error is comming....")

    else:
        fm = SignIn()
    return render(request,'verify/signin.html',{"forms": fm})

