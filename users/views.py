from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import AgregarForm

def login_view(request):
    if(request.method == "POST"):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("inventory:list-view")
    else:
        if request.user.is_authenticated:
            return redirect("inventory:list-view")
        else:
            form = AuthenticationForm(request)
    return render(request, 'login.html', {'form':form})


def logout_view(request):
    logout(request)
    return redirect('users:login')