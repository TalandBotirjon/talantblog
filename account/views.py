from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == "POST":

        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"{user.username}. You are Register and login this site.")
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def loginview(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f"{username}. You are login site.")
            return redirect("/")
    return render(request, 'account/login.html')


def logoutview(request):
    logout(request)
    return redirect("/")
