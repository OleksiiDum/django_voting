from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    voted = models.IntegerField()

    def voted(self):
        self.voted += 1
        
