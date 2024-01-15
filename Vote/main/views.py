from django.shortcuts import render
from .models import Vote

# Create your views here.
def index(request):
    return render(request, 'main/index.html', {
        "votes": Vote.objects.all()
    })

def vote(request):
    return render(request, 'main/vote.html')