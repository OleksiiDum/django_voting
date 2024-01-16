from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('create_user', views.create_user, name='create_user'),
    path('authenticate_user', views.authenticate_user, name='authenticate_user')
]
