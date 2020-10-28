from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def Signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                username = fm.cleaned_data.get('username')
                messages.success(
                    request, f'Account created Successfully for {username}.')
                fm.save()
        else:
            fm = SignupForm()
        return render(request, 'Auth/signup.html', {'form': fm})
    else:
        return HttpResponseRedirect('/newsfeed/')


# Login
def Login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                name = fm.cleaned_data['username']
                pw = fm.cleaned_data['password']
                user = authenticate(username=name, password=pw)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/newsfeed/')
        else:
            fm = AuthenticationForm()
        return render(request, 'Auth/login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/newsfeed/')
# Logout
@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# change password with older None
@login_required
def Change_Password(request):
    if request.method == 'POST':
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = PasswordChangeForm(user=request.user)
    return render(request, 'Auth/change_password.html', {'form': fm})
