from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('siteapp:index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('siteapp:index')
            else:
                messages.error(request, 'Invalid Credentials!!!')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def signout(request):
    logout(request) 
    return redirect('login')


@login_required(login_url='login')
def changepasssword(request):
    return render(request, 'change_password.html')
