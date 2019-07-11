from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class User(AbstractUser):
    gender = models.PositiveIntegerField(null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    profile = models.ImageField(upload_to='user_image/profile/%Y/%m/%d', blank=True)
