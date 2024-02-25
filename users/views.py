from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm 

def login_if_valid(request, username, password):
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/authentication.html")
    
    return render(request, "users/welcome.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        login_if_valid(request, username, password)
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("users:index"))
        else:  
            return render(request, "users/login.html", {
                "message" : "Invalid Credentials!",
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message" : "Logged out!",
    })

def register_view(request):
    if (request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            login_if_valid(request, username, password)
            return redirect('users:index')
        else:
            return render(request, 'users/register.html', {
                'form' : form
            })
    
    form = UserCreationForm()
    return render(request, 'users/register.html', {
        'form' : form
    })