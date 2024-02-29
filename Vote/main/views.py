from django.shortcuts import render
from .models import Vote
from authentication.models import CustomUser
from django.contrib.auth.decorators import  login_required

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {
        "votes": Vote.objects.all(),
        "users": CustomUser.objects.all()
    })

def vote(request):
    return render(request, 'main/vote.html')

def create_voting(request):
    if request.method != "POST":
        return render(request, 'main/create_voting.html')
    else:
        header = request.POST.get("header")
        description = request.POST.get("description")
        voting = Vote(header=header, description=description)
        voting.save()