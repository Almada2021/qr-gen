from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("qrs:list")
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', { "form": form})

def login_view(request):
    if request.method == "POST":
        # print(request.POST.next)
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next'in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("qrs:list")
        
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect("home")

@login_required(login_url="/users/login")
def account_view(request):
    return render(request, 'users/account.html')