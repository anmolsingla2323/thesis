from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

def home(request):
    return render(request, 'loginpage.html')

def fp(request):
    return render(request, 'fp.html')

def el(request):
    return render(request, 'examinor.html')

def al(request):
    return render(request, 'admin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        examinor = request.POST['choice']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('el')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('home')

def logout(request):
    auth.logout(request)
    return('/', request)