from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Todo(models.Model):
    content = models.TextField()