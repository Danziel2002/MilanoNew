from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    level = models.IntegerField(default = 0)
    experience = models.IntegerField(default = 0)
    recycleManager = models.BooleanField(default = False)