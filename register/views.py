
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from .forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('indexf')
        else:
            print(form.errors)  # Print form errors for debugging purposes
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
        else:
            print(form.errors)  # Print form errors for debugging purposes
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})
