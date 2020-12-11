from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    return render(request, 'home.html')

def course(request):
    return render(request, 'course-single.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        branch = request.POST['branch']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, ' Bravo! Your GateEasy account has been created successfully.')
        return redirect('signin')
    else:
        messages.info(request, 'Please make an account to join GateEasy.')
        return redirect('homepage')

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Hello! Welcome to GateEasy...')
            return redirect('homepage')
        else:
            messages.error(request, 'Hey, Incorrect Credentials.')
            return redirect('homepage')
    else:
        messages.info(request, 'If you already have an account, Please Sign In.')
        return redirect('homepage')

def UserLogout(request):
    logout(request)
    messages.success(request, 'You have been Logged Out successfully.')
    return redirect('homepage')

def signin(request):
    return render(request, 'signin.html')

def contact(request):
    messages.success(request, 'GateEasy team will contact you soon.')
    return redirect('homepage')
