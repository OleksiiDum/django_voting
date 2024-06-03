from django.shortcuts import render, redirect
from .models import Voting, Vote
from authentication.models import CustomUser
from django.contrib.auth.decorators import  login_required
# from django.http import JsonResponse
# import segno
from .logs import logger


# qrcode = segno.make('Yellow Submarine')
# qrcode.save('yellow-submarine.png')


# Create your views here.
def index(request):
    logger.info("Opened main page")
    return render(request, 'main/index.html', {
        "votes": Voting.objects.all(),
        "users": CustomUser.objects.all()
    })

@login_required(login_url='login')
def vote_page(request, voting_id):
    logger.info("Opened voting page")
    voting = Voting.objects.filter(id=voting_id)[0]
    votes = Vote.objects.filter(voter=request.user, voting_id=voting)
    context = {"voting": voting, "voted": False}
    if len(votes) > 0:
        context["voted"] = True
    if request.method == "POST":
        choise = request.POST.get("vote")
        vote = Vote(choise=choise=="yes", voting_id=voting, voter=request.user)
        vote.save()
        logger.info("User has voted")
        context["voted"] = True
    return render(request, 'main/vote.html', context)

@login_required(login_url='login')
def create_voting(request):
    if request.method != "POST":
        logger.info("Opened create_voting page")
        return render(request, 'main/create_voting.html')
    else:
        logger.info(dict(request.POST.lists()))
        header = request.POST.get("header")
        description = request.POST.get("description")
        if not header or not description:
            return render(request, 'main/create_voting.html', {"error": "Empty Header or Description"})
        user = request.user
        voting = Voting(header=header, description=description, user_id=user)
        voting.save()
        logger.info("Created voting")
        return redirect("index")

@login_required
def user_page(request):
    if request.method == "GET":
        return render(request, 'main/user_page.html')