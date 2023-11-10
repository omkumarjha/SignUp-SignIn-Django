from django.shortcuts import render
from .forms import SignUp
# Create your views here.

def home(request):
    return render(request,'verify/home.html')

def signup(request):
    fm = SignUp()
    return render(request,'verify/signup.html',{"forms":fm})
    
def signin(request):
    return render(request,'verify/signin.html')

