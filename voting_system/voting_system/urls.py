from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Vote/', include('Vote.urls')),
    path('admin/', admin.site.urls),
]
