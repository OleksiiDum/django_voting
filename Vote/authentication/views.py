from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect, Http404
from .models import CustomUser
from .forms import LoginForm, CustomUserForm
from django.contrib.auth import authenticate, login, logout
from.logs import logger


# Create your views here.
def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            logger.info("User is logged in")
            return render(request, 'main/index.html')
    else:
        logger.info("Opened login page")
        form = LoginForm
    return render(request, 'auth/login.html', {"form": form})

def logout_user(request):
    logger.info("User is logged out")
    logout(request)
    return redirect('index')

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
        logger.info("Opened register page")
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info("User is registered")
            return redirect('login')

    context = {'form': form}

    return render(request, 'auth/register.html', context)

def authenticate_user(request):
    if request.method == "POST":
        email = request.POST.get("email_field")
        password = request.POST.get("password_field")
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            logger.info("User is authenticated")
            login(request, user)
            return redirect("index")
        else:
            logger.warning("User not exists")
            return redirect('login') #send notification to user whyredirect
