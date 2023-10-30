from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import RegistationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    message = {}
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            message = {'error' : 'Password is Incorrect'}
    return render(request, 'signin.html', message)


def user_logout(request):
    logout(request)
    return redirect('login')

def user_profile(request, id):
    user = User.objects.get(pk=id)
    
    return render(request, 'profile.html', {'name' : user.username, 'email':user.email})


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # Update the session to keep the user logged in
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile', request.user.id)  # Redirect to a profile page or any other desired URL
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_pass.html', {'form': form})