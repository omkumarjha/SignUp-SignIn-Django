from django.shortcuts import render
from .forms import SignUp
# Create your views here.

def home(request):
    return render(request,'verify/home.html')

def signup(request):
    fm = SignUp()
    return render(request,'verify/signup.html',{"form":fm})
    
def signin(request):
    return HttpResponse("It is a Sign In page by Om Kumar")

