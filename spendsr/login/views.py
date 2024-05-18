from django.shortcuts import render,redirect
from .forms import UserForm,UserRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
def homepage(request):
    return render(request,'homescreen.html')

def viewregister(request):
    return render(request,'register.html')

def viewlogin(request):
    return render(request,'login.html')


def checklogin(request):

    user_name = request.POST['user_name']
    password = request.POST['password']
    user = authenticate(request,username=user_name,password=password)
    if user is None:
        return HttpResponse('Please sign up!')
    else:
        login(request, user)
        return redirect('/')
