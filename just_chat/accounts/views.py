from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    return render(request, 'accounts/signup.html')

def signin(request):
    return render(request, 'accounts/signin.html')

@login_required(login_url='signin')
def signout(request):
    logout(request.user)
    return redirect('signin')