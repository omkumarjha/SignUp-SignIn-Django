from django.shortcuts import render,redirect
from .forms import SignUp , SignIn
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from myproject import settings

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

            # agar jo user apne aap ko register kar raha hai uski already entry present hai database ke andar to usko error ke sath redirect kardo 
            if User.objects.filter(username=name):
                messages.error(request,"Username already Exists !. Try some other username")
                return redirect("signup")

            if User.objects.filter(email=email):
                messages.error(request,"Email already Exists !. Try some other email")
                return redirect("signup")

            # We have a module User . jiska humne object create kara hai aur because yeh entries hum database mai save karne wale hai to first apne ko sare current migrations ko migrate karna hoga and then we can create user account and show them ki aapka account crete ho chuka hai abb login kariye 

            myuser = User.objects.create_user(name,email,password)
            myuser.save()


            # sending Welcome Email

            subject = "Welcome to Om's Website"
            message = "Hello " + name + "!! \n" + "Welcome to My Website!! \nThank you for visiting our website\n\n Thanking you \n Om Kumar Jha"
            from_email = settings.EMAIL_HOST_USER
            to_email = [email]  # to_email list or tuple ki form mai hota hai
            send_mail(subject,message,from_email,to_email,fail_silently = True) # fail_silently means agar email send nhi ho pata to usse website crash nhi honi chaiye.

            messages.success(request,"Your account has been successfully created. We have send you a welcome email !")

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
                return redirect("signin")


        else:
            print("Error is comming....")

    else:
        fm = SignIn()
    return render(request,'verify/signin.html',{"forms": fm})


# below method tab chalega jab user ne logout button pe click kara hai 
def handlelogout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect("home")
