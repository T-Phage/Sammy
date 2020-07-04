from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from suiteapp.forms import *
from suiteapp.models import *


# Create your views here.
def signin(request):
    if request.user.is_authenticated:
        return redirect('suiteapp:index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('suiteapp:index')
            else:
                messages.error(request, 'Invalid Credentials or account not available !!!')
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def signout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def changepasssword(request):
    return render(request, 'change_password.html')


# def register(request):
#     if request.method == 'POST':
#         firstname = request.POST['username']
#         surname = request.POST['surname']
#         othername = request.POST['othername']
#         username = request.POST['username']
#         email = request.POST['email']
#         gender = request.POST['gender']
#         department = request.POST['department']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#
#         user = MyUser.objects.create_user(firstname=firstname, username=username, email=email, department=department,
#                                           password=password2, surname=surname, gender=gender,
#                                           othername=othername,
#                                           )
#         user.save()
#         return redirect('login')
#     else:
#         userform = UserCreationForm()
#         context = {'userform': userform}
#         return render(request, 'register.html', context)

def register(request):
    if request.method == 'POST':
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
            return redirect('login')
    else:
        userform = UserCreationForm()
        context = {'userform': userform}
        return render(request, 'register.html', context)
