from django.shortcuts import render,redirect
from .forms import SignUp , SignIn
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'verify/home.html')

def signup(request):
    if request.method == "POST":
        fm = SignUp(request.POST)

        if fm.is_valid():
            print("Form is validated successfully ")

            name = fm.cleaned_data["name"]
            email = fm.cleaned_data["email"]
            password = fm.cleaned_data["password"]

            # We have a module User . jiska humne object create kara hai aur because yeh entries hum database mai save karne wale hai to first apne ko sare current migrations ko migrate karna hoga and then we can create user account and show them ki aapka account crete ho chuka hai abb login kariye 

            myuser = User.objects.create_user(name,email,password)
            myuser.save()

            messages.success(request,"Your account has been successfully created.")

            return redirect("signin")

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

            name = fm.cleaned_data["name"]
            password = fm.cleaned_data["password"]
            
            # Agar user nae signin page pe credentials sahi diye hai to user object retrn hoga othewise none return hoga
            user = authenticate(username=name,password=password)

            if user is not None:
                login(request,user)
                return render(request,"verify/loggedin.html",{"name":name})
            else:
                messages.error(request,"Bad Credentials")
                print("Bad ")
                return redirect("signin")


        else:
            print("Error is comming....")

    else:
        fm = SignIn()
    return render(request,'verify/signin.html',{"forms": fm})

