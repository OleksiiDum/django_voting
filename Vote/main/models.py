from django.db import models
from authentication.models import User

# Create your models here.
class Vote(models.Model):
    name = models.CharField(max_length=200)
    answer = models.BooleanField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def repr(self):
        return self.name