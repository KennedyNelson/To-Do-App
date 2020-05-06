from django.db import models
from django.contrib.auth.models import User

class Activity(models.Model):
    title = models.CharField(max_length=100)
    crossed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    activities = models.ManyToManyField(Activity, blank=True)

    def __str__(self):
        return self.user.username
