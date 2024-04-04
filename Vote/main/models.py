from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Voting(models.Model):
    header = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def repr(self):
        return self.header

class Vote(models.Model):
    choise = models.BooleanField()
    voting_id = models.ForeignKey(Voting, on_delete=models.CASCADE)
    voter = models.ForeignKey(CustomUser,on_delete=models.CASCADE)