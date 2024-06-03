from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('votings/<int:voting_id>', views.vote_page, name='vote_page'),
    path('create_voting', views.create_voting, name='create_voting'),
    path('user_page', views.user_page, name='user_page')
]
