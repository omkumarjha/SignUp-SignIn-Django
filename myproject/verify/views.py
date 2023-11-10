from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'verify/home.html')

def signup(request):
    return HttpResponse("It is a Sign up page by Om Kumar")

def signin(request):
    return HttpResponse("It is a Sign In page by Om Kumar")

