from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from .models import User
from .forms import RegisterForm, LoginForm

# Create your views here.
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request, 'main/index.html')
    else:
        form = LoginForm
    return render(request, 'auth/login.html', {"form": form})

def logout(request):
    pass

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["your_name"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = User.objects.create(name=name, email=email, password=password)
            user.save()
            return render(request, 'main/index.html')
    else:
        form = RegisterForm
    return render(request, 'auth/register.html', {"form": form})

def create_user(request):
    if request.method == "POST":
        email = request.get()
        password = request.get()
        return render(request, 'main/index.html')

def authenticate_user(request):
    if request.method == "POST":
        pass
