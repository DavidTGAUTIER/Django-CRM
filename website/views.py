from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            message.success(request, "You have been logged in !")
            return redirect('home')
        
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logout_user(request):
    pass