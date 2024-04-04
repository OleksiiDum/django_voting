from django.contrib import admin
from .models import Voting

# Register your models here.
class VotingAdmin(admin.ModelAdmin):
    fields = ["user_id", "header"]


admin.site.register(Voting, VotingAdmin)
