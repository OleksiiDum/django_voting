from django.shortcuts import render
from .models import Vote
from django.contrib.auth.decorators import  login_required

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {
        "votes": Vote.objects.all()
    })

def vote(request):
    return render(request, 'main/vote.html')