from django.shortcuts import render, HttpResponseRedirect
from .form import signupForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def signup(request):
    if request.method == "POST":
        fm = signupForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'The account has been added')
    else:
        fm = signupForm()
    return render(request, 'signup.html', {'form': fm})


def ulogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/p/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/p/')


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/l/')


def ulogout(request):
    logout(request)
    return HttpResponseRedirect('/s/')