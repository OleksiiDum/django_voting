from django.db import models
from authentication.models import CustomUser

# Create your models here.
class Vote(models.Model):
    header = models.CharField(max_length=200, null=False)
    description = models.TextField(null=False)
    choise = models.BooleanField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def repr(self):
        return self.header